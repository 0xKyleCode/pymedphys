import numpy as np
from scipy.optimize import curve_fit, leastsq, fmin
from sys import maxsize

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import log, pow, pi, sin, cos
from itertools import groupby
from operator import itemgetter
from scipy.interpolate import interp1d
from skimage.filters import threshold_otsu


def uncert_err_sigfig(ufloat_input, nsig=1):
    assert isinstance(nsig, int)
    return ("{:.%su}" % nsig).format(ufloat_input)


def uncert_err_relative(ufloat_input, nsig=1):
    nv = ufloat_input.nominal_value
    st = ufloat_input.std_dev

    rel_err = 1.0 * st / nv

    dist = int(log(abs(rel_err), 10)) - nsig
    rel_err_sig = round(rel_err / pow(10, dist)) * pow(10, dist)

    abs_err_sig = nv * rel_err_sig
    nd_abs = -1 * int(log(abs(abs_err_sig), 10))
    nvstr = r"%0." + str(nd_abs) + "e"
    # print(nvstr)

    return nv, rel_err_sig


def gauss_1D(x, *p):
    A, mu, sigma = p
    return A * np.exp(-((x - mu) ** 2) / (2.0 * sigma**2))


def fit_1d_gauss(ydata, mean_guess, sig_guess, xdata=None):
    # Define some test data which is close to Gaussian
    # data = ydata
    # hist, bin_edges = numpy.histogram(data, density=True)
    # bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2

    if xdata is None:
        xdata = np.arange(0, len(ydata))

    # p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
    p0 = [np.max(ydata), mean_guess, sig_guess]

    coeff, var_matrix = curve_fit(gauss_1D, xdata, ydata, p0=p0)

    # Get the fitted curve
    hist_fit = gauss_1D(xdata, *coeff)

    # plt.plot(xdata, ydata, label='Test data')
    # plt.plot(xdata, hist_fit, label='Fitted data')

    # Finally, lets get the fitting parameters, i.e. the mean and standard deviation:
    print("Fitted mean = ", coeff[1])
    print("Fitted standard deviation = ", coeff[2])

    A, mu, sig = coeff

    return A, mu, sig


def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    width_x = float(width_x)
    width_y = float(width_y)

    toret = lambda x, y: height * np.exp(
        -(((center_x - x) / width_x) ** 2 + ((center_y - y) / width_y) ** 2) / 2
    )
    return np.vectorize(toret)


# #def fit_2d_gauss(data):
#
#
#     def moments(data):
#         """Returns (height, x, y, width_x, width_y)
#         the gaussian parameters of a 2D distribution by calculating its
#         moments """
#         total = data.sum()
#         X, Y = np.indices(data.shape)
#         x = (X * data).sum() / total
#         y = (Y * data).sum() / total
#         col = data[:, int(y)]
#         width_x = np.sqrt(np.abs((np.arange(col.size) - x) ** 2 * col).sum() / col.sum())
#         row = data[int(x), :]
#         width_y = np.sqrt(np.abs((np.arange(row.size) - y) ** 2 * row).sum() / row.sum())
#         height = data.max()
#         return height, x, y, width_x, width_y
#
#         """Returns (height, x, y, width_x, width_y)
#         the gaussian parameters of a 2D distribution found by a fit"""
#
#     params = moments(data)
#     errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) - data)
#     from scipy.optimize import leastsq
#     p, success = leastsq(errorfunction, params)
#     return p


def fit_3d_gauss(nd_vox_obj, mean_guess, sigma_guess, lower_threshold=None):
    """
    fit 3d gaussian to NDVoxel object
    :param nd_vox_obj:
    :param mean_guess: list of guesses for gaussian mean
    :param sigma_guess:  list of guesses for gaussian std dev
    :param lower_threshold: value below which to ignore data set
    :return:
    """

    # translate coordinate system guess into index on array guess
    gx, gy, gz = nd_vox_obj.coord_tuple_to_nearest_index(mean_guess)
    # translate coordinate system width to number of voxels
    gsx, gsy, gsz = sigma_guess / np.array(nd_vox_obj.voxdims)

    if lower_threshold is not None:
        data = np.ma.masked_less(nd_vox_obj, lower_threshold)
    else:
        data = nd_vox_obj

    def gaussian(height, center_x, center_y, center_z, width_x, width_y, width_z):
        """Returns a gaussian function with the given parameters"""
        return lambda x, y, z: height * np.exp(
            -(
                ((center_x - x) / width_x) ** 2
                + ((center_y - y) / width_y) ** 2
                + ((center_z - z) / width_z) ** 2
            )
            / 2
        )

    def fitgaussian(data, params):
        """Returns (height, x, y, width_x, width_y)
        the gaussian parameters of a 2D distribution found by a fit"""

        errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) - data)

        p, success = leastsq(errorfunction, params, ftol=1e-4, xtol=1e-4)
        return p

    params = fitgaussian(data, params=(np.max(data), gx, gy, gz, gsx, gsy, gsz))

    (height, x, y, z, width_x, width_y, width_z) = params

    x, y, z = nd_vox_obj.index_tuple_to_coord([x, y, z])

    return (x, y, z), (width_x, width_y, width_z)


def fit_2d_gauss(
    nd_vox_obj, mean_guess, sigma_guess, lower_threshold=None, show_plot=False
):
    """
    fit 3d gaussian to NDVoxel object
    :param nd_vox_obj:
    :param mean_guess: list of guesses for gaussian mean
    :param sigma_guess:  list of guesses for gaussian std dev
    :param lower_threshold: value below which to ignore data set, or 'otsu' for otsu bg thresh
    :return:
    """

    # translate coordinate system guess into index on array guess
    gx, gy = nd_vox_obj.coord_tuple_to_nearest_index(mean_guess)
    # translate coordinate system width to number of voxels
    gsx, gsy = sigma_guess / np.array(nd_vox_obj.voxdims)

    if lower_threshold is None:
        data = nd_vox_obj
    elif lower_threshold == "otsu":

        def otsu_threshold(pa, show_plot=False):
            thresh = threshold_otsu(pa)
            # print(thresh)
            image = pa
            thresh = threshold_otsu(pa)
            binary = pa < thresh
            if show_plot:
                fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
                ax = axes.ravel()
                ax[0] = plt.subplot(1, 3, 1)
                ax[1] = plt.subplot(1, 3, 2)
                ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])
                ax[0].imshow(image, cmap=plt.cm.gray)
                ax[0].set_title("Original")
                ax[0].axis("off")
                ax[1].hist(image.ravel(), bins=256)
                ax[1].set_title("Histogram")
                ax[1].axvline(thresh, color="r")
                ax[2].imshow(binary, cmap=plt.cm.gray)
                ax[2].set_title("Thresholded")
                ax[2].axis("off")
                plt.show()
            return thresh

        lower_threshold = otsu_threshold(nd_vox_obj, show_plot=show_plot)
        data = np.ma.masked_less(nd_vox_obj, lower_threshold)
    else:
        data = np.ma.masked_less(nd_vox_obj, lower_threshold)

    def gaussian(height, center_x, center_y, width_x, width_y):
        """Returns a gaussian function with the given parameters"""
        return lambda x, y: height * np.exp(
            -(((center_x - x) / width_x) ** 2 + ((center_y - y) / width_y) ** 2) / 2
        )

    def fitgaussian(data, params):
        """Returns (height, x, y, width_x, width_y)
        the gaussian parameters of a 2D distribution found by a fit"""

        errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) - data)

        p, success = leastsq(errorfunction, params, ftol=1e-4, xtol=1e-4)
        return p

    params = fitgaussian(data, params=(np.max(data), gx, gy, gsx, gsy))

    (height, x, y, width_x, width_y) = params
    print("height: {}->{}".format(np.max(data), height))
    x, y = nd_vox_obj.index_tuple_to_coord([x, y])
    sy = width_y * data.voxdims[1]
    sx = width_x * data.voxdims[1]

    # print(x,y,sx,sy)

    if show_plot:
        fig, ax = plt.subplots()

        # sy = width_y
        # sx = width_x
        ax.imshow(data, **nd_vox_obj.PLOT_KWARGS)
        ax.add_artist(Ellipse((y, x), sy, sx, facecolor=None, ec="r", fill=False))
        ax.add_artist(
            Ellipse((y, x), 2 * sy, 2 * sx, facecolor=None, ec="r", fill=False)
        )

        ax.plot([y], [x], "+r")
        plt.show()

    return (x, y), (sx, sy), gaussian(height, x, y, sx, sy)


def most_common_in_target_list(target_values, value_list_to_search):
    """
    returns the most common
    :param target_values: target values to match list members
    :param value_list_to_search: list of values to find most common target value
    :return:
    """
    value_list_to_search = [int(s) for s in value_list_to_search]
    most_common_int = max(set(value_list_to_search), key=value_list_to_search.count)
    closest_to = target_values[
        np.argmin([np.abs(trg - most_common_int) for trg in target_values])
    ]

    return closest_to


def get_consecutive_groups(iterable_to_group, buffer_pad=None):
    """
    get consecutive integer groups in a list ie: [1,2,3,7,8,9] => [[1,2,3],[7,8,9]]
    :param list:
    :return:
    """
    if buffer_pad is not None:
        iterable_to_group = list(iterable_to_group)

        diffs = np.ediff1d(iterable_to_group, to_begin=[0])

        to_add = np.where((diffs > 1) & (diffs <= buffer_pad))

        for ind in to_add[0]:
            iterable_to_group.insert(ind, iterable_to_group[ind] - 1)

    bp_groups = []

    for key, group in groupby(
        enumerate(iterable_to_group), lambda index, item: index - item
    ):
        group = map(itemgetter(1), group)
        bp_groups.append(group)
    return bp_groups


def linear_map_range(xl0, xh0, xl1, xh1):
    """
    Linear mapping from one range to another
    :rtype: linear mapping function [xl0,xh0] -> [xl1,xh1]
    """
    assert xh0 > xl0 and xh1 > xl1
    return lambda s: ((s - xl0) / (xh0 - xl0)) * (xh1 - xl1) + xl1


def calc_nonuniform_dist_function(sampling_array, range_min, range_max):
    """
    Given discrete array representing probability dist (sampling_array) and range limits,
    calculate commulative to find uniform distribution
    :param sampling_array: sampling array
    :param range_min: minimum range for input
    :param range_max: max range for input
    :return: function converting [range_min,range_max] (uniform) -> [range_min, range_max] (dist sampled uniform)
    """
    cumulitive = np.cumsum(sampling_array)

    gmin, gmax = np.min(cumulitive), np.max(cumulitive)

    dens_func = interp1d(cumulitive, range(0, len(cumulitive)))

    gmap = linear_map_range(range_min, range_max, gmin, gmax)
    ginv = linear_map_range(0, len(cumulitive) - 1, range_min, range_max)

    return lambda s: ginv(dens_func(gmap(s)))


def rot_matrix_func(angle_deg):
    """
    build 2d rotation matrix given angle in degrees
    :param angle_deg:
    :return:
    """
    a = np.deg2rad(angle_deg)
    return np.array([[np.cos(a), -1 * np.sin(a)], [np.sin(a), np.cos(a)]])


def rotate_point_pairs(point_pair_list, angle):
    """
    rotate list of point-pairs
    :param point_pair_list: list of form [(x0,y0), (x1,y1)...]
    :param angle: angle to rotate
    :return: list of rotated coordinate pairs
    """
    x_y = np.array(point_pair_list).flatten()
    x_y = np.array(list(zip(*[iter(x_y)] * 2)))

    R = rot_matrix_func(angle)

    rotated = [np.dot(R, s) for s in x_y]

    return list(zip(*[iter(rotated)] * 2))


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """

    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array(
        [
            [aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
            [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
            [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc],
        ]
    )


def calc_closest_approach(l0, l1, p0):
    """

    :param l0: point1 defining line
    :param l1: point2 defining line
    :param p0: point to calculate closest approach
    :return:
    """
    p1 = np.array(l0)
    p2 = np.array(l1)
    p3 = np.array(p0)

    u = (p1 - p2) / np.linalg.norm(p1 - p2)

    i = (p2) - np.dot(p2 - p3, u) * u
    d = np.linalg.norm(i - p3)

    return d, i


def findFuncMax(function, guess, guessMin=None, guessMax=None):
    def toMin(x):
        if guessMax is not None and x > guessMax:
            return maxsize
        if guessMin is not None and x < guessMin:
            return maxsize

        return -1.0 * function(x)

    return fmin(toMin, guess, disp=False)[0]


def findNearestArrayVal(inArray, val):
    inArray = np.array(inArray)

    idx = np.argmin(np.abs(inArray - val))

    return idx


def divideWithZero(numerator, denominator, lowDenomClip=None, zeroDivideReplace=0):
    """
    divide two numpy arrays, yielding zero when the denominator is zero
    :param numerator
    :param denominator
    :param lowDenomClip - if denominator is below this value, set to zero
    :param zeroDivideReplace - replace all denominator = 0 values in diision with this number
    """

    if lowDenomClip is not None:
        denominator[np.where(denominator < lowDenomClip)] = 0

    with np.errstate(divide="ignore"):
        result = numerator / denominator
        result[denominator == 0] = zeroDivideReplace

    return result


def dpi_to_mm_reso(dpi):
    return (1.0 / dpi) * 25.4


def percent_diff_1d(xspace, yfunc1, yfunc2, absolute=False, min_thershold_frac_max=0.1):
    """
    percentage difference including min thresholding
    :param xspace:
    :param yfunc1:
    :param yfunc2:
    :param absolute:
    :param min_thershold:
    :return xspace, yspace
    """

    assert np.shape(yfunc1) == np.shape(yfunc2)

    # if np.shape(yfunc1) != np.shape(xspace) and np.shape(yfunc1)[1] == 1:
    #     yfunc1 = yfunc1[:, 0]
    #     yfunc2 = yfunc2[:, 0]
    #
    # elif np.shape(yfunc1) != np.shape(xspace):
    #     raise NotImplementedError()

    assert len(xspace) == len(yfunc1) == len(yfunc2)

    valid_x = slice(None, None, None)

    if min_thershold_frac_max > 0:
        max_y = np.max(np.concatenate((yfunc1, yfunc2)))
        thresh = min_thershold_frac_max * max_y
        valid_x = np.where((yfunc1 > thresh) & (yfunc2 > thresh))

    try:
        xspace = np.array(xspace)[valid_x]
    except IndexError:
        xspace = np.array(xspace)[valid_x[0]]
    yfunc1 = yfunc1[valid_x]
    yfunc2 = yfunc2[valid_x]

    if absolute:
        yspace = np.abs(yfunc1 - yfunc2) / np.abs(np.mean([yfunc1, yfunc2], axis=0))
    else:
        yspace = (yfunc1 - yfunc2) / np.mean([yfunc1, yfunc2], axis=0)

    return xspace, yspace


def rotatedRectWithMaxArea(w, h, angle):
    """
    Given a rectangle of size wxh that has been rotated by 'angle' (in
    degrees), computes the width and height of the largest possible
    axis-aligned rectangle (maximal area) within the rotated rectangle.
    """
    if w <= 0 or h <= 0:
        return 0, 0

    angle = angle * 2 * pi / 360

    width_is_longer = w >= h
    side_long, side_short = (w, h) if width_is_longer else (h, w)

    # since the solutions for angle, -angle and 180-angle are all the same,
    # if suffices to look at the first quadrant and the absolute values of sin,cos:

    sin_a, cos_a = abs(sin(angle)), abs(cos(angle))
    if side_short <= 2.0 * sin_a * cos_a * side_long or abs(sin_a - cos_a) < 1e-10:
        # half constrained case: two crop corners touch the longer side,
        #   the other two corners are on the mid-line parallel to the longer line
        x = 0.5 * side_short
        wr, hr = (x / sin_a, x / cos_a) if width_is_longer else (x / cos_a, x / sin_a)
    else:
        # fully constrained case: crop touches all 4 sides
        cos_2a = cos_a * cos_a - sin_a * sin_a
        wr, hr = (w * cos_a - h * sin_a) / cos_2a, (h * cos_a - w * sin_a) / cos_2a

    return wr, hr
