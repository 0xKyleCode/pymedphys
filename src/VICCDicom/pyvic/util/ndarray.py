"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

Authors: Clay Lindsay and Mark Baker
"""

import numpy as np
from scipy.ndimage import median_filter
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from typing import Tuple, List, Union, Optional, Callable

from pyvic.util.data_structures import NDVoxelArray
from pyvic.util.plotting import plot_box
from pyvic.util.utils import accepts
from pyvic.util.image import otsu_threshold
from pyvic.util.numeric import gauss_1D


@accepts(NDVoxelArray)
def crop_nan(array: "NDVoxelArray") -> "NDVoxelArray":
    """
    Crops the provided NDVoxel array to remove columns and rows that are entirely NaN.

    Args:
        array (NDVoxelArray): The NDVoxel array to crop.

    Returns:
        NDVoxelArray: Cropped NDVoxel array.
    """

    nans = np.isnan(array)
    nancols = np.all(nans, axis=0)
    nanrows = np.all(nans, axis=1)

    firstcol = nancols.argmin()
    firstrow = nanrows.argmin()

    lastcol = len(nancols) - nancols[::-1].argmin()
    lastrow = len(nanrows) - nanrows[::-1].argmin()

    return array.subset_by_index([(firstrow, lastrow), (firstcol, lastcol)])


@accepts(NDVoxelArray)
def coordmax(nd_voxel_obj: NDVoxelArray) -> Tuple[int]:
    """
    Converts the index of the maximum value of an NDVoxelArray object
    to its corresponding coordinate.

    Parameters:
    - nd_voxel_obj (NDVoxelArray): The NDVoxelArray object.

    Returns:
    - tuple: Coordinate corresponding to the maximum value.
    """
    return nd_voxel_obj.index_tuple_to_coord(nd_argmax(nd_voxel_obj))


@accepts(np.ndarray)
def nd_argmax(ndarray_obj: np.ndarray) -> Tuple[int]:
    """
    Finds the index of the maximum value in a numpy ndarray.

    Parameters:
    - ndarray_obj (np.ndarray): The numpy ndarray.

    Returns:
    - tuple: Index of the maximum value.
    """
    return np.unravel_index(np.argmax(ndarray_obj), ndarray_obj.shape)


@accepts(NDVoxelArray)
def central_subset(
    nd_voxel_obj: NDVoxelArray,
    center_coordinates: List[int],
    subset_size: Union[int, List[int]],
    do_clipping: bool = False,
) -> NDVoxelArray:
    """
    Gets a subset of the NDVoxelArray around the given center coordinates.

    Parameters:
    - nd_voxel_obj (NDVoxelArray): The NDVoxelArray object.
    - center_coordinates (List[int]): List of center coordinates for the subset.
    - subset_size (Union[int, List[int]]): Size of the subset. Can be a single integer
                                          or a list of two integers.
    - do_clipping (bool, optional): Whether to clip values. Default is False.

    Returns:
    - NDVoxelArray: Subset of the original NDVoxelArray.
    """

    if isinstance(subset_size, int):
        cent_subset = [
            (s - subset_size, s + subset_size) for d, s in enumerate(center_coordinates)
        ]

    elif len(subset_size) == 2:
        cent_subset = [
            (s - subset_size[0], s + subset_size[1])
            for d, s in enumerate(center_coordinates)
        ]
    else:
        raise NotImplementedError(
            " central subset only implremented for 2d and integer"
        )

    return nd_voxel_obj.subset(cent_subset, do_clipping=do_clipping)


def rot90_3d(nd_vox_obj: NDVoxelArray, vector: List[int]) -> np.ndarray:
    """
    Performs a 3D orthogonal rotation around axes on the given NDVoxelArray.

    Parameters:
    - nd_vox_obj (NDVoxelArray): The NDVoxelArray object.
    - vector (List[int]): Vector indicating the direction of rotation.

    Returns:
    - np.ndarray: Rotated 3D array.
    """
    rot_axis = np.where(np.abs(vector) == 1)

    rot_axis = rot_axis[0][0]

    sign = np.sign(vector[rot_axis])

    if sign == -1:
        toRet = rot90_3d(nd_vox_obj, np.abs(vector))
        toRet = rot90_3d(toRet, np.abs(vector))
        return rot90_3d(toRet, np.abs(vector))

    plane_rotation = range(0, 3)
    plane_rotation.remove(rot_axis)

    assert np.all([vector[s] == 0 for s in plane_rotation])

    slc = [slice(None), slice(None), slice(None)]
    slc[plane_rotation[1]] = slice(None, None, -1)

    return np.swapaxes(nd_vox_obj, *plane_rotation)[slc]


def find_voxel_bbox(vox_struct: np.ndarray, vox_num: int) -> List[List[int]]:
    """
    Gets the bounding box of a subset of voxels in an array.

    Parameters:
    - vox_struct (np.ndarray): Voxel array.
    - vox_num (int): Target voxel number for determining bounds.

    Returns:
    - List[List[int]]: Bounding box dimensions.
    """
    vox_inds = np.where(vox_struct == vox_num)

    return [[np.min(s), np.max(s)] for s in vox_inds]


def find_voxel_center(vox_struct: np.ndarray) -> np.ndarray:
    """
    Returns the central voxel of a structure.

    Parameters:
    - vox_struct (np.ndarray): Voxel structure.

    Returns:
    - np.ndarray: Central voxel of the structure.
    """
    return np.rint(np.array(np.shape(vox_struct)) / 2.0).astype(np.int16)


def find_voxel_subset_center(vox_struct: np.ndarray, vox_num: int) -> np.ndarray:
    """
    Returns the central voxel of a structure subset.

    Parameters:
    - vox_struct (np.ndarray): Voxel structure.
    - vox_num (int): Target voxel number.

    Returns:
    - np.ndarray: Central voxel of the structure subset.
    """
    bbox = find_voxel_bbox(vox_struct, vox_num)
    slcs = [slice(s[0], s[1] + 1) for s in bbox]
    # print(np.shape(vox_struct[slcs]))
    cent = find_voxel_center(vox_struct[slcs])

    cent = cent + np.array([s[0] for s in bbox])

    return cent


class NDVoxelFitter:
    """
    A class dedicated to various fitting operations on NDVoxel data.
    """

    @classmethod
    def fit_1d_gauss(
        cls,
        ydata: np.ndarray,
        mean_guess: float,
        sig_guess: float,
        xdata: Optional[np.ndarray] = None,
    ) -> Tuple[float, float, float]:
        """
        Fit a 1D Gaussian function to provided ydata.

        Args:
            ydata (np.ndarray): The Y data to fit.
            mean_guess (float): Initial guess for the Gaussian mean.
            sig_guess (float): Initial guess for the Gaussian standard deviation.
            xdata (Optional[np.ndarray], optional): The X data corresponding to ydata. Defaults to None.

        Returns:
            Tuple[float, float, float]: Returns the amplitude, mean, and standard deviation of the fitted Gaussian.
        """
        if xdata is None:
            xdata = np.arange(0, len(ydata))

        p0 = [np.max(ydata), mean_guess, sig_guess]

        coeff, _ = curve_fit(gauss_1D, xdata, ydata, p0=p0)

        A, mu, sig = coeff

        return A, mu, sig

    @classmethod
    def fit_2d_gauss(
        cls,
        nd_vox_obj: "NDVoxelArray",
        mean_guess: List[float],
        sigma_guess: List[float],
        lower_threshold: Optional[Union[float, str]] = None,
        show_plot: bool = False,
    ) -> Tuple[Tuple[float, float], Tuple[float, float], Callable]:
        """
        Fit a 2D Gaussian function to the provided NDVoxel object.

        Args:
            nd_vox_obj ('NDVoxelArray'): The NDVoxel object to fit.
            mean_guess (List[float]): Initial guesses for the Gaussian means in x and y.
            sigma_guess (List[float]): Initial guesses for the Gaussian standard deviations in x and y.
            lower_threshold (Optional[Union[float, str]], optional): Value below which to ignore dataset or use 'otsu' for background thresholding. Defaults to None.
            show_plot (bool, optional): If True, displays a plot of the fit. Defaults to False.

        Returns:
            Tuple[Tuple[float, float], Tuple[float, float], Callable]: Returns the means, standard deviations, and the Gaussian function of the fitted data.
        """

        # translate coordinate system guess into index on array guess
        gx, gy = nd_vox_obj.coord_tuple_to_nearest_index(mean_guess)
        # translate coordinate system width to number of voxels
        gsx, gsy = sigma_guess / np.array(nd_vox_obj.voxdims)

        if lower_threshold is None:
            data = nd_vox_obj
        elif lower_threshold == "otsu":
            lower_threshold = otsu_threshold(nd_vox_obj, show_plot=show_plot)
            data = np.ma.masked_less(nd_vox_obj, lower_threshold)
        else:
            data = np.ma.masked_less(nd_vox_obj, lower_threshold)

        def gaussian(
            height: float,
            center_x: float,
            center_y: float,
            width_x: float,
            width_y: float,
        ) -> Callable[[float, float], float]:
            """
            Define a 2D Gaussian function with the given parameters.

            Args:
                height (float): Maximum height (amplitude) of the Gaussian.
                center_x (float): x-coordinate of the center of the Gaussian.
                center_y (float): y-coordinate of the center of the Gaussian.
                width_x (float): Width (standard deviation) of the Gaussian along the x-direction.
                width_y (float): Width (standard deviation) of the Gaussian along the y-direction.

            Returns:
                Callable: A lambda function representing the 2D Gaussian.
            """
            return lambda x, y: height * np.exp(
                -(((center_x - x) / width_x) ** 2 + ((center_y - y) / width_y) ** 2) / 2
            )

        def fitgaussian(
            data: np.ndarray, params: Tuple[float, float, float, float, float]
        ) -> Tuple[float, float, float, float, float]:
            """
            Fit the provided data using a Gaussian function and return the parameters.

            Args:
                data (np.ndarray): The 2D data array to fit.
                params (Tuple): Initial guesses for the Gaussian parameters in the order: (height, center_x, center_y, width_x, width_y).

            Returns:
                Tuple: The optimized parameters for the Gaussian fit.
            """
            errorfunction = lambda p: np.ravel(
                gaussian(*p)(*np.indices(data.shape)) - data
            )
            p, success = leastsq(errorfunction, params, ftol=1e-4, xtol=1e-4)
            return p

        params = fitgaussian(data, params=(np.max(data), gx, gy, gsx, gsy))
        (height, x, y, width_x, width_y) = params

        x, y = nd_vox_obj.index_tuple_to_coord([x, y])
        sy = width_y * data.voxdims[1]
        sx = width_x * data.voxdims[0]

        if show_plot:
            fig, ax = plt.subplots()
            ax.imshow(data, **nd_vox_obj.PLOT_KWARGS)
            ax.add_artist(Ellipse((y, x), sy, sx, facecolor=None, ec="r", fill=False))
            ax.add_artist(
                Ellipse((y, x), 2 * sy, 2 * sx, facecolor=None, ec="r", fill=False)
            )
            ax.plot([y], [x], "+r")
            plt.show()

        return (y, x), (sy, sx), gaussian(height, y, x, sy, sx)

    def fit_3d_gauss(
        cls,
        nd_vox_obj: "NDVoxelArray",
        mean_guess: List[float],
        sigma_guess: List[float],
        lower_threshold: Optional[Union[float, str]] = None,
    ) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        """
        Fit a 3D Gaussian function to the provided NDVoxel object.

        Args:
            nd_vox_obj (NDVoxelArray): The NDVoxel object to fit.
            mean_guess (List[float]): Initial guesses for the Gaussian means in x, y, and z.
            sigma_guess (List[float]): Initial guesses for the Gaussian standard deviations in x, y, and z.
            lower_threshold (Optional[Union[float, str]]): Value below which to ignore dataset. If set to a string, it indicates a specific thresholding method. Defaults to None.

        Returns:
            Tuple[Tuple[float, float, float], Tuple[float, float, float]]: Returns the means and standard deviations of the fitted data.
        """

        # translate coordinate system guess into index on array guess
        gx, gy, gz = nd_vox_obj.coord_tuple_to_nearest_index(mean_guess)
        # translate coordinate system width to number of voxels
        gsx, gsy, gsz = sigma_guess / np.array(nd_vox_obj.voxdims)

        if lower_threshold is not None:
            data = np.ma.masked_less(nd_vox_obj, lower_threshold)
        else:
            data = nd_vox_obj

        def gaussian(
            height: float,
            center_x: float,
            center_y: float,
            center_z: float,
            width_x: float,
            width_y: float,
            width_z: float,
        ) -> Callable[[float, float, float], float]:
            """
            Define a 3D Gaussian function with the given parameters.

            Args:
                ... : Descriptions of each parameter (similar to the above documentation format).

            Returns:
                Callable: A lambda function representing the 3D Gaussian.
            """
            return lambda x, y, z: height * np.exp(
                -(
                    ((center_x - x) / width_x) ** 2
                    + ((center_y - y) / width_y) ** 2
                    + ((center_z - z) / width_z) ** 2
                )
                / 2
            )

        def fitgaussian(
            data: np.ndarray,
            params: Tuple[float, float, float, float, float, float, float],
        ) -> Tuple[float, float, float, float, float, float, float]:
            """
            Fit the provided 3D data using a Gaussian function and return the parameters.

            Args:
                data (np.ndarray): The 3D data array to fit.
                params (Tuple): Initial guesses for the Gaussian parameters.

            Returns:
                Tuple: The optimized parameters for the Gaussian fit.
            """
            errorfunction = lambda p: np.ravel(
                gaussian(*p)(*np.indices(data.shape)) - data
            )
            p, success = leastsq(errorfunction, params, ftol=1e-4, xtol=1e-4)
            return p

        params = fitgaussian(data, params=(np.max(data), gx, gy, gz, gsx, gsy, gsz))

        (height, x, y, z, width_x, width_y, width_z) = params
        x, y, z = nd_vox_obj.index_tuple_to_coord([x, y, z])

        return (x, y, z), (width_x, width_y, width_z)

    @classmethod
    def ndvox_deformation_fit(
        cls, template_ndvox: "NDVoxelArray", ndvox_to_fit: "NDVoxelArray"
    ) -> Callable[[float, float], float]:
        """
        Fit the `ndvox_to_fit` to the template provided by `template_ndvox` using a deformation model.

        Args:
            template_ndvox (NDVoxelArray): The NDVoxel object that serves as the template.
            ndvox_to_fit (NDVoxelArray): The NDVoxel object to be fitted to the template.

        Returns:
            Callable[[float, float], float]: A function representing the fitted deformation.

        Raises:
            NotImplementedError: If the dimension of the template NDVoxel is not 2.
            RuntimeError: If the least-squares optimization fails.
        """
        if template_ndvox.nDim != 2:
            raise NotImplementedError()

        # Interpolation function from the template
        interp_func = template_ndvox.interp2d()

        def test_func(p: List[float]) -> Callable[[float, float], float]:
            """
            Deformed function based on the provided parameters.

            Args:
                p (List[float]): Parameters for the deformation (height scale, width in x and y, and translation in x and y).

            Returns:
                Callable[[float, float], float]: A lambda function representing the deformed version.
            """
            A, u, v, dx, dy = p
            return lambda x, y: A * interp_func(u * (x + dx), v * (y + dy))

        p0 = [1, 1, 1, 0, 0]

        errorfunction = lambda p: np.ravel(
            test_func(p)(
                ndvox_to_fit.coordinate_mesh[1], ndvox_to_fit.coordinate_mesh[0]
            )
            - ndvox_to_fit
        )

        p, success = leastsq(errorfunction, p0, ftol=1e-4, xtol=1e-4)

        if success:
            return test_func(p)
        else:
            raise RuntimeError(
                "Least-squares optimization failed in finding deformed function."
            )

    @classmethod
    def ndvox_normalize_fit(
        cls, template_ndvox: "NDVoxelArray", ndvox_to_fit: "NDVoxelArray"
    ) -> Callable[[float, float], float]:
        """
        Normalize the `ndvox_to_fit` based on the template provided by `template_ndvox`.

        Args:
            template_ndvox (NDVoxelArray): The NDVoxel object that serves as the template.
            ndvox_to_fit (NDVoxelArray): The NDVoxel object to be normalized based on the template.

        Returns:
            Callable[[float, float], float]: A function representing the normalized version of ndvox_to_fit.

        Raises:
            NotImplementedError: If the dimension of the template NDVoxel is not 2.
            RuntimeError: If the least-squares optimization fails.
        """
        if template_ndvox.nDim != 2:
            raise NotImplementedError()

        # Interpolation function from the template
        interp_func = template_ndvox.interp2d()

        def test_func(p: float) -> Callable[[float, float], float]:
            """
            Normalized function based on the provided parameter.

            Args:
                p (float): Parameter for normalization (height scale).

            Returns:
                Callable[[float, float], float]: A lambda function representing the normalized version.
            """
            A = p
            return lambda x, y: A * interp_func(x, y)

        p0 = 1

        errorfunction = lambda p: np.ravel(
            test_func(p)(
                ndvox_to_fit.coordinate_mesh[1], ndvox_to_fit.coordinate_mesh[0]
            )
            - ndvox_to_fit
        )

        p, success = leastsq(errorfunction, p0, ftol=1e-4, xtol=1e-4)

        if success:
            return test_func(p)
        else:
            raise RuntimeError(
                "Least-squares optimization failed in finding normalized function."
            )

    @classmethod
    def find_2d_area_around_max(
        cls,
        area_to_search: "NDVoxelArray",
        fraction_of_max: float,
        median_filter_size: Optional[int] = None,
        show_plot: bool = False,
    ) -> Tuple[float, float, float, float]:
        """
        Find the 2D area around the maximum value in the provided NDVoxel object.

        Args:
            area_to_search (NDVoxelArray): The NDVoxel object to search within.
            fraction_of_max (float): Fraction of the maximum value to be considered for contour.
            median_filter_size (int, optional): Size of the median filter. If provided, the area will be filtered before processing. Defaults to None.
            show_plot (bool, optional): If True, displays a plot of the area. Defaults to False.

        Returns:
            Tuple[float, float, float, float]: Bounding box dimensions around the maximum (xmin, xmax, ymin, ymax).
        """

        if median_filter_size is not None:
            area_to_contour = NDVoxelArray(
                median_filter(area_to_search, median_filter_size),
                origin=area_to_search.origin,
                voxdims=area_to_search.voxdims,
            )
        else:
            area_to_contour = area_to_search

        norm_level = np.max(area_to_contour)

        X, Y = np.meshgrid(
            area_to_search.coordinate_mesh[1], area_to_search.coordinate_mesh[0]
        )

        if show_plot:
            fig, ax = plt.subplots()
            cs = ax.contour(
                X, Y, area_to_contour, levels=[fraction_of_max * norm_level]
            )
            verts = cs.collections[0].get_paths()[0].vertices
            ymin, ymax = np.min([s[1] for s in verts]), np.max([s[1] for s in verts])
            xmin, xmax = np.min([s[0] for s in verts]), np.max([s[0] for s in verts])
            plot_box(ax, xmin, xmax, ymin, ymax)
            plt.show()
        else:
            fig, ax = plt.subplots()
            cs = ax.contour(
                X, Y, area_to_contour, levels=[fraction_of_max * norm_level]
            )
            verts = cs.collections[0].get_paths()[0].vertices
            ymin, ymax = np.min([s[1] for s in verts]), np.max([s[1] for s in verts])
            xmin, xmax = np.min([s[0] for s in verts]), np.max([s[0] for s in verts])
            plt.close()

        return xmin, xmax, ymin, ymax
