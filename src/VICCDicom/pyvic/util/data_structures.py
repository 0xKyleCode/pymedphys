#!/usr/bin/env python
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
from __future__ import annotations
import logging
from uncertainties import ufloat

# import h5py
from typing import List
import numpy as np
from numpy.core.multiarray import ndarray

from pyvic.util.file import (
    LoadableObj,
    csv_to_tuple,
    array_tuple_to_csv,
    DataFrameableCollectable,
)
from pyvic.util.numeric import divideWithZero, findNearestArrayVal, findFuncMax


_logger = logging.getLogger(__name__)


class NDVoxelArray(DataFrameableCollectable, np.ndarray):
    ZAXIS, YAXIS, XAXIS = 0, 1, 2
    #
    AXIS_NAMES = ["z", "y", "x"]

    _PLOT_KWARGS = {"origin": "lower"}

    def __new__(
        cls, input_array, voxdims=None, origin=None, info=None, **kwargs
    ) -> NDVoxelArray:
        import time

        import copy

        if isinstance(input_array, np.ndarray):
            obj = input_array.view(NDVoxelArray)
        else:
            obj = np.asarray(input_array)
            obj = obj.view(NDVoxelArray)

        if voxdims is not None:
            assert len(np.shape(obj)) == len(voxdims)
            obj.voxdims = tuple([float(s) for s in voxdims])
        else:
            # Default voxel size is 1
            obj.voxdims = np.ones(len(np.shape(input_array)))

        if origin is not None:
            assert len(np.shape(obj)) == len(origin)
            obj.origin = origin

        else:
            # Default origin is 0,..
            obj.origin = np.zeros(len(np.shape(input_array)))

        if info is not None:
            obj.info = info
        else:
            obj.info = {}

        # bnds = [(obj.origin[s], obj.origin[s] + np.shape(obj)[s] * obj.voxdims[s]) for s in range(0, len(np.shape(obj)))]
        # obj._extent = [bnds[1][0],bnds[1][1],bnds[0][0],bnds[0][1]]

        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None:
            return
        self.voxdims = getattr(obj, "voxdims", None)
        self.origin = getattr(obj, "origin", None)
        self.info = getattr(obj, "info", None)
        # print(self.origin,self.extent)

    def __reduce__(self):
        # Get the parent's __reduce__ tuple
        pickled_state = super().__reduce__()
        # Create our own tuple to pass to __setstate__
        new_state = pickled_state[2] + (self.voxdims, self.origin, self.info)
        # Return a tuple that replaces the parent's __setstate__ tuple with our own
        return (pickled_state[0], pickled_state[1], new_state)

    def __setstate__(self, state):
        self.voxdims = state[-3]  # Set the info attribute
        self.origin = state[-2]  # Set the info attribute
        self.info = state[-1]
        # Call the parent's __setstate__ with the other tuple elements.
        super().__setstate__(state[0:-3])

    def __iadd__(self, other):
        if isinstance(other, NDVoxelArray) and len(other.shape) > 0:
            # print(other.voxdims, other.origin, other.shape)
            assert self.voxdims == other.voxdims
            assert self.origin == other.origin
            assert self.shape == other.shape
            return self + other
        else:
            return super().__iadd__(other)

    def half_vox(self, dim):
        return self.voxdims[dim] / 2.0

    @staticmethod
    def from_ndvoxel(template, data):
        assert isinstance(template, NDVoxelArray)
        assert isinstance(data, ndarray)
        import copy

        return NDVoxelArray(
            data,
            voxdims=template.voxdims,
            origin=template.origin,
            info=copy.deepcopy(template.info),
        )

    @property
    def PLOT_KWARGS(self):
        return {**self._PLOT_KWARGS, "extent": self.extent}

    @property
    def bounds(self):
        return [
            (self.origin[s], self.origin[s] + np.shape(self)[s] * self.voxdims[s])
            for s in range(0, len(np.shape(self)))
        ]

    @property
    def center(self):
        return [(s[1] - s[0]) / 2.0 + s[0] for s in self.bounds]

    @property
    def extent(self):
        bnds = self.bounds
        return [bnds[1][0], bnds[1][1], bnds[0][0], bnds[0][1]]

    @property
    def nDim(self):
        return len(self.voxdims)

    @property
    def physicalDim(self):
        return self.evalDim(np.shape(self))

    @property
    def physicalVol(self):
        return np.prod(self.physicalDim)

    @property
    def voxel_edge_mesh(self):
        return tuple(
            [
                np.linspace(
                    self.origin[i],
                    self.origin[i] + self.voxdims[i] * (self.shape[i]),
                    self.shape[i] + 1,
                )
                for i in range(0, self.nDim)
            ]
        )

    @property
    def coordinate_mesh(self, dim=None) -> list[list[float]]:
        to_ret = []

        for i in range(0, self.nDim):
            to_ret.append(self.get_coordinate_mesh(i))
            # to_ret.append(np.linspace(self.origin[i]+self.half_vox(i),
            #                           self.origin[i]+self.voxdims[i]*self.shape[i]-self.half_vox(i),
            #                           self.shape[i], endpoint=True))
        return to_ret

    def get_coordinate_mesh(self, dim: int) -> list[float]:
        assert dim < self.nDim
        return np.linspace(
            self.origin[dim] + self.half_vox(dim),
            self.origin[dim] + self.voxdims[dim] * self.shape[dim] - self.half_vox(dim),
            self.shape[dim],
            endpoint=True,
        )

    @property
    def coordinate_array(self) -> tuple[list[float]]:
        return np.meshgrid(*self.coordinate_mesh, indexing="ij")

    def evalDim(self, shapeTuple):
        return np.array(shapeTuple) * np.array(self.voxdims)

    def evalRectVolume(self, rectSizeTuple):
        return np.prod(self.evalDim(rectSizeTuple))

    def evalVoxValueVolume(self, value):
        return len(np.where(self == value)[0]) * np.prod(self.voxdims)

    def get_mid_point(self):
        pass

    def interp2d(self, kind="cubic"):
        from scipy import interpolate

        if self.nDim == 2:
            return interpolate.interp2d(
                self.coordinate_mesh[1], self.coordinate_mesh[0], self, kind=kind
            )
        else:
            raise NotImplementedError()

    def interp_to_NDVoxel(
        self, target_interp_vox: NDVoxelArray, interp_kind: str = "cubic"
    ) -> NDVoxelArray:
        if self.nDim == 2 and target_interp_vox.nDim == 2:
            bs = self.bounds
            bt = target_interp_vox.bounds

            if not all(s[0] <= t[0] and s[1] >= t[1] for s, t in zip(bs, bt)):
                # print(bs, target_interp_vox.bounds)
                # raise NotImplementedError('target coord system must be within bounds of NDVoxel')
                pass

            int_data = self.interp2d(kind=interp_kind)(
                target_interp_vox.coordinate_mesh[1],
                target_interp_vox.coordinate_mesh[0],
            )

            return NDVoxelArray(
                int_data,
                origin=target_interp_vox.origin,
                voxdims=target_interp_vox.voxdims,
            )

        else:
            raise NotImplementedError()

    def crop_to_NDVoxel(self, target_crop_vox: NDVoxelArray) -> NDVoxelArray:
        if self.nDim == 2 and target_crop_vox.nDim == 2:
            bs = self.bounds
            bt = target_crop_vox.bounds
            print(bt)

            if not all(s[0] <= t[0] and s[1] >= t[1] for s, t in zip(bs, bt)):
                raise NotImplementedError(
                    "target coord system must be within bounds of NDVoxel"
                )

            return self.subset(bt)

        else:
            raise NotImplementedError()

    def resample(self, new_vox_dims, zoom_order=3) -> NDVoxelArray:
        zoom_factor = np.array(self.voxdims) / np.array(new_vox_dims)

        import scipy.ndimage

        new_eye_vol = scipy.ndimage.zoom(self, zoom_factor, order=zoom_order)

        return NDVoxelArray(
            new_eye_vol,
            voxdims=np.array(self.voxdims) / zoom_factor,
            origin=self.origin,
        )

    # def resample2(self, new_vox_dims, zoom_order=3) -> NDVoxelArray:
    #
    #     zoom_factor = np.array(self.voxdims) / np.array(new_vox_dims)
    #
    #     import scipy.ndimage
    #     new_eye_vol = scipy.ndimage.zoom(self, zoom_factor, order=zoom_order)
    #
    #     return NDVoxelArray(new_eye_vol, voxdims=np.array(self.voxdims) / zoom_factor, origin=self.origin)

    def index_to_coord(self, index, dimension):
        assert dimension >= 0 and dimension < len(self.shape)
        assert index >= 0 and index < self.shape[dimension]
        return self.origin[dimension] + (index + 0.5) * self.voxdims[dimension]

    def index_tuple_to_coord(self, index_list):
        assert len(index_list) == len(self.shape)
        return [self.index_to_coord(cent, ind) for ind, cent in enumerate(index_list)]

    def center_index(self):
        return [int(s / 2.0) for s in self.shape]

    def real_coord(self, index, dimension):
        assert index <= self.shape[dimension] and index >= 0
        return self.origin[dimension] + (index * self.voxdims[dimension])

    def coord_to_nearest_index(self, coord, dimension, do_clipping=False):
        """
        :param coord:
        :param dimension:
        :param do_clipping: if true, and subset is larger than parent array, return maximum size subset
        :return:
        """
        assert dimension >= 0 and dimension < len(self.shape)

        # if coordinate outside of array, return maximum / minimum of array coords
        if do_clipping:
            if coord < self.origin[dimension]:
                coord = self.origin[dimension]
            if coord > self.bounds[dimension][1]:
                coord = self.bounds[dimension][1]
        else:
            assert (
                coord >= self.origin[dimension] and coord <= self.bounds[dimension][1]
            )

        return int(np.floor((coord - self.origin[dimension]) / self.voxdims[dimension]))

    def fraction_to_coord(self, fraction, dimension):
        """
        Returns coordinate value for given fraction from lower edge of image
        :param fraction: decimal on 0->1 representing fraction of distance from edge of image
        :param dimension: index of desired coordinate (z,y,x) = (0,1,2)
        :return: coordinate representation of distance from edge
        """
        assert 0.0 <= fraction <= 1.0
        return (
            self.origin[dimension]
            + fraction * self.voxdims[dimension] * self.shape[dimension]
        )

    def fraction_to_nearest_index(self, fraction, dimension, do_clipping=False):
        """
        Returns nearest index for given fraction from lower edge of image
        :param fraction: decimal on 0->1 representing fraction of distance from edge of image
        :param dimension: index of desired coordinate (z,y,x) = (0,1,2)
        :return: coordinate representation of distance from edge
        """
        assert 0.0 <= fraction <= 1.0
        return self.coord_to_nearest_index(
            self.fraction_to_coord(fraction, dimension),
            dimension,
            do_clipping=do_clipping,
        )

    def coord_tuple_to_nearest_index(self, coord_list):
        assert len(coord_list) == len(self.shape)
        return [
            self.coord_to_nearest_index(coord, ind)
            for ind, coord in enumerate(coord_list)
        ]

    def npy_index_list_to_coords(self, index_list):
        """

        :param index_list: List of array indeces of the form [[z1,z2,...],[y1,y2..],[x1,x2...]]
        :return: list of coordinate of the same form
        """

        assert len(index_list) == self.nDim

        nindex = len(index_list[0])

        #  make sure all index lists are same size
        assert all([len(s) == nindex for s in index_list])

        return [
            [self.index_tuple_to_coord(index_list[i][j]) for j in range(0, nindex)]
            for i in range(0, self.nDim)
        ]

    def subset(self, coord_bounds: list, do_clipping: bool = False):
        """
        Generate subset of voxel array
        :param coord_bounds: list of tuples of the form [ (low,high), ..., len(self.shape)]
        :param do_clipping: if true, and subset is larger than parent array, return maximum size subset
        :return: sub image defined by low,high coordinates
        """

        assert len(coord_bounds) == len(self.shape)
        # for l, h in coord_bounds:
        #     assert l < h

        ind_lims = []

        for d in range(0, len(coord_bounds)):
            try:
                l, h = coord_bounds[d]
            except TypeError:
                l = coord_bounds[d]
                h = coord_bounds[d]

            li = self.coord_to_nearest_index(l, d, do_clipping=do_clipping)

            nv = int(np.ceil((h - l) / self.voxdims[d]))

            # throw error if a larger than array subset is requested
            if li + nv > self.shape[d] and not do_clipping:
                raise RuntimeError(
                    "requested subset of %s voxels in dimension %s is larger than parent array dimension %s"
                    % (li + nv, d, self.shape[d])
                )

            ind_lims = ind_lims + [(li, li + nv)]

        return self.subset_by_index(ind_lims, do_clipping=do_clipping)

    def subset_by_percent(
        self, percent_bounds: list[tuple(float)], do_clipping: bool = False
    ) -> NDVoxelArray:
        """
        Generate subset of image with percent boundbox
        :param percent_bounds: list of tuples with bounding box percentages eg [ (cor1_low, cor1_high)... ]
        :param do_clipping: if true, and subset is larger than parent array, return maximum size subset
        :return:
        """

        assert len(percent_bounds) == len(self.shape)

        bb = []
        for d in range(0, len(percent_bounds)):
            l, h = percent_bounds[d]

            assert l < h and l >= 0 and h <= 1

            min, max = 0, self.shape[d]  # self.bounds[d]
            length = max - min
            bb.append((min + length * l, min + length * h))

        return self.subset_by_index(bb, do_clipping=do_clipping)

    # def coords_from_image_fraction(self):

    def subset_by_index(self, coord_bounds: list, do_clipping: bool = False):
        """
        Generate subset of voxel array
        :param coord_bounds: list of tuples of the form [ (low,high), ..., len(self.shape)]
        :param do_clipping: if true, and subset is larger than parent array, return maximum size subset
        :return: sub image defined by low,high coordinates # type: NDVoxelArray
        """

        assert len(coord_bounds) == len(self.shape)

        this_origin = []
        ind_lims = []
        voxdim_lims = []

        for d in range(0, len(coord_bounds)):
            try:
                l, h = coord_bounds[d]
            except TypeError:
                if isinstance(coord_bounds[d], int):
                    l = coord_bounds[d]
                    h = coord_bounds[d]
                else:
                    raise NotImplementedError()

            assert l <= h

            li = int(l)

            lo = self.index_to_coord(li, d) - (self.voxdims[d] / 2.0)

            nv = int(h - l)

            # throw error if a larger than array subset is requested
            if li + nv > self.shape[d] and not do_clipping:
                raise RuntimeError(
                    "requested subset of %s voxels in dimension %s is larger than parent array dimension %s"
                    % (li + nv, d, self.shape[d])
                )

            if nv > 1:
                ind_lims = ind_lims + [slice(li, li + nv)]
                voxdim_lims = voxdim_lims + [self.voxdims[d]]
                this_origin = this_origin + [lo]
            else:
                ind_lims = ind_lims + [li]

        return NDVoxelArray(
            self[tuple(ind_lims)], voxdims=voxdim_lims, origin=this_origin
        )  # type: NDVoxelArray

    def slice_3D_to_2D(self, slice_dim, slice_index, do_clipping=False) -> NDVoxelArray:
        if not self.nDim == 3:
            raise NotImplementedError(
                "slice_3D_to_2D only implemented for 3D NDVoxelArray"
            )

        coord_bounds = [[0, self.shape[s]] for s in range(0, self.nDim)]
        coord_bounds[slice_dim] = slice_index

        return self.subset_by_index(coord_bounds, do_clipping=do_clipping)

    def to_dataframe_dict(self):
        # return {'input_array': self.view(np.array), 'voxdims': self.voxdims, 'origin': self.origin, 'info': None}
        return {
            "input_array": self.tolist(),
            "voxdims": self.voxdims,
            "origin": self.origin,
            "info": None,
        }

    @classmethod
    def from_dataframe_dict(cls, df_dict):
        # print("from_dataframe_dict")

        toret = NDVoxelArray(
            df_dict["input_array"],
            voxdims=df_dict["voxdims"],
            origin=df_dict["origin"],
            info=df_dict["info"],
        )
        return toret

    @property
    def stats(self) -> str:
        retstr = (
            "%s: %s\n"
            "\tvox_size: %s\n"
            "\torigin: %s\n"
            "\tsize: %s"
            % (
                self.__class__.__name__,
                self.shape,
                self.voxdims,
                self.origin,
                self.physicalDim,
            )
        )
        return retstr


class DataSet1D(LoadableObj):
    (X, Y, Z) = 0, 1, 2

    def __init__(self, x, y, err=None):
        try:
            assert len(x) == len(y)
        except:
            print(
                "ERROR: inputs x,y must be arrays of the same length (%s != %s)"
                % (len(x), len(y))
            )
            raise

        self.x = np.array(x)
        self.y = np.array(y)
        self.err = None
        if err is not None:
            self.err = np.array(err)

        self.sort()

        pass

    @property
    def domain(self):
        return self.x[0], self.x[-1]

    def getPartition(self, partXPoints, underCut=False):
        partXPoints = sorted(partXPoints)

        # check that partition points are stricly inside data set
        assert partXPoints[0] > self.x[0] and partXPoints[-1] < self.x[-1]

        nearestArgs = [self.getNearestXArg(x) for x in partXPoints]

        if nearestArgs[0] != 0:
            nearestArgs = np.concatenate(([0], nearestArgs))
        if nearestArgs[-1] != len(self.x):
            nearestArgs = np.concatenate((nearestArgs, [len(self.x)]))

        return [
            slice(nearestArgs[i] + 1, nearestArgs[i + 1])
            for i in range(0, len(nearestArgs) - 1)
        ]

    def addAbsXUncert(self, absXUncert):
        """
        add absolute X uncertainty (delY = d/dx (f) * delX)
        :param absXUncert: absolute uncertainty for x param
        """

        grad = np.gradient(self.y)
        fullUncert = grad * absXUncert

        if self.err is None:
            self.err = divideWithZero(fullUncert, self.y)
        else:
            absErr = self.absError

            fullAbsErr = [
                np.sqrt(absErr[s] ** 2 + fullUncert[s] ** 2)
                for s in range(0, len(self.err))
            ]

            self.err = divideWithZero(fullAbsErr, self.y)

        return self

    def __add__(self, toAdd):
        assert np.array_equal(self.x, toAdd.x)

        newX = self.x
        newY = self.y + toAdd.y
        newErr = np.zeros(len(self.x))

        nonZero = np.where(newY != 0)
        newErr[nonZero] = (
            np.sqrt(self.absError[nonZero] ** 2 + toAdd.absError[nonZero] ** 2)
            / newY[nonZero]
        )

        return DataSet1D(newX, newY, newErr)

    def __div__(self, denominator):
        assert isinstance(denominator, DataSet1D)
        assert np.array_equal(self.x, denominator.x)

        newX = self.x
        newY = self.y
        newErr = np.zeros(len(self.x))

        divSlice = np.where(denominator.y != 0)
        newY[divSlice] = newY[divSlice] / denominator.y[divSlice]

        newErr = np.sqrt(self.err**2 + denominator.err**2)

        return DataSet1D(newX, newY, newErr)

        newErr = np.zeros(len(self.x))

    def getPlotData(self):
        return [(self.x, self.y)]

    def insert(self, x, y, err=None):
        import bisect

        insertInd = bisect.bisect_left(self.x, x)

        self.x = np.insert(self.x, insertInd, x)
        self.y = np.insert(self.y, insertInd, y)

        if err is not None and self.err is not None:
            self.err = np.insert(self.err, insertInd, err)

    @property
    def absError(self):
        return self.err * self.y

    @classmethod
    def fromSum(cls, ds1DListToSum):
        x = ds1DListToSum[0].x
        avY = np.array(
            [np.average([s.y[i] for s in ds1DListToSum]) for i in range(0, len(x))]
        )
        stdY = np.array(
            [np.std([s.y[i] for s in ds1DListToSum]) for i in range(0, len(x))]
        )
        nonZer = np.where(avY != 0)
        err = np.zeros(np.shape(x))
        err[nonZer] = stdY[nonZer] / avY[nonZer]
        return DataSet1D(x, avY, err)

    @classmethod
    def fromDetector(
        cls, detectorObj, axis=None, xLims=None, yLims=None, zLims=None, voxMid=True
    ):
        if axis == None:
            axis = DataSet1D.Z

        if not isinstance(detectorObj, list):
            detObjList = [detectorObj]
        else:
            detObjList = detectorObj

        totX, totY, totErr = (np.array([]), np.array([]), np.array([]))

        for detectorObj in detObjList:
            logging.debug(detectorObj)

            logging.debug("DetectorData:%s", str(detectorObj.data))

            (x, y, err) = detectorObj.project1D(
                axis, xLims=xLims, yLims=yLims, zLims=zLims, voxMid=voxMid
            )

            totX = np.concatenate((totX, x))
            totY = np.concatenate((totY, y))
            totErr = np.concatenate((totErr, err))

        return DataSet1D(totX, totY, totErr)

    @classmethod
    def fromTupleList(cls, xyTupleList):
        # no error provided
        if len(xyTupleList[0]) == 2:
            uz = zip(*xyTupleList)
            x, y = uz[0], uz[1]
            return DataSet1D(x, y)
        # error provided
        else:
            uz = zip(*xyTupleList)
            x, y, e = uz[0], uz[1], uz[2]
            return DataSet1D(x, y, e)

    @classmethod
    def fromDataFile(cls, dataFname, xCol=0, yCol=7, errCol=None, sep=None):
        if errCol is None:
            (x, y) = csv_to_tuple(dataFname, [xCol, yCol], sep)
            return DataSet1D(x, y, None)
        else:
            (x, y, err) = csv_to_tuple(dataFname, [xCol, yCol, errCol], sep)
            return DataSet1D(x, y, err)

    @classmethod
    def fromFlairDatFile(cls, dataFname):
        xlow, xhigh, val, err = csv_to_tuple(dataFname, [0, 1, 2, 3], delChar=None)

        xmid = (xlow + xhigh) / 2

        return DataSet1D(xmid[:-1], val[:-1], err[:-1] / 100)

    #         if errCol is None:
    #             (x,y) =  csv2Tuple(dataFname, [xCol,yCol], sep)
    #             return DataSet1D(x,y, None)
    #         else:
    #             (x,y,err) =  csv2Tuple(dataFname, [xCol,yCol,errCol], sep)
    #             return DataSet1D(x,y, err)

    @classmethod
    def fromWeightedData(cls, dataSet1DList, weights):
        total = None
        xSamp = None

        for ind, ds in enumerate(dataSet1DList):
            if total is None:
                total = ds.y * weights[ind]
                xSamp = ds.x
            else:
                total += ds.y * weights[ind]

        return DataSet1D(xSamp, total)

    @classmethod
    def fromSampledDatasets(cls, dataSetList):
        """
        generate data set from samples on same experiment, take error as std deviation
        :param dataSetList: list of dataset1d to combine
        """

        x = dataSetList[0].x
        y = np.average([ds.y for ds in dataSetList], axis=0)
        err = np.std([ds.y for ds in dataSetList], axis=0)

        return cls(x, y, err / y)

    @property
    def reso(self):
        return self.x[1] - self.x[0]

    def resample(self, res, interpKind="cubic"):
        raise RuntimeError("will crash if non equal spaced X")

        dsLen = self.x[-1] - self.x[0]
        nSamp = dsLen / res

        mesh = np.linspace(self.x[0], self.x[-1], nSamp, endpoint=True)

        return self.interpTo(mesh, kind=interpKind)

    def getYVal(self, xpos):
        return self.interp()(xpos)

    def scaleX(self, mult, offset_to_zero=False):
        if offset_to_zero:
            x0 = self.x[0]
            self.x = (self.x - x0) * mult + x0
        else:
            self.x = self.x * mult

        return self

    def scaleY(self, mult):
        self.y = self.y * mult
        return self

    def scaleYByBin(self, scaleList):
        self.y = self.y * scaleList
        return self

    def offsetX(self, offset):
        self.x = self.x + offset
        return self

    def offsetY(self, offset):
        self.y = self.y + offset
        return self

    def crop(self, xlow, xhigh, inplace=True):
        ind = self._getIndexInclusive(xlow, xhigh)

        if inplace:
            self.y = self.y[ind]
            self.x = self.x[ind]

            if self.err is not None:
                self.err = self.err[ind]

            return self
        else:
            if self.err is not None:
                return DataSet1D(self.x[ind], self.y[ind], self.err[ind])
            else:
                return DataSet1D(self.x[ind], self.y[ind])

    def getRange(self, xlims):
        """
        return DataSet1D containing data points within specified x limits
        :param xlims: tuple (xlow, xhigh)
        """

        xlow, xhigh = xlims

        assert self.x[0] <= xlow <= self.x[-1]
        assert self.x[0] <= xhigh <= self.x[-1]
        assert xlow <= xhigh

        lowInd = np.where(self.x >= xlow)[0][0]
        highInd = np.where(self.x > xhigh)[0][0]

        #         lowInd = np.argmin(np.abs(self.x - xlow))
        #         highInd = np.argmin(np.abs(self.x - xhigh))
        subRange = slice(lowInd, highInd)

        if self.err is not None:
            return DataSet1D(self.x[subRange], self.y[subRange], self.err[subRange])
        else:
            return DataSet1D(self.x[subRange], self.y[subRange])

    def sort(self):
        if self.err is not None:
            ez = zip(self.x, self.err)
            ez = sorted(ez)

        z = zip(self.x, self.y)
        z = sorted(z)

        self.x = np.array([s[0] for s in z])
        self.y = np.array([s[1] for s in z])

        if self.err is not None:
            self.err = np.array([s[1] for s in ez])

    def fullPrep(self, xOffset, xScale, xLow, xHigh, normed=True):
        #         raise DeprecationWarning

        self.sort()

        self.offsetX(xOffset)
        self.scaleX(xScale)

        self.crop(xLow, xHigh)

        if normed:
            self.norm()

    def score(self, scoreFunc):
        scoreFunc = np.vectorize(scoreFunc)
        return self.y * scoreFunc(self.x)

    def scoreErr(self, scoreFunc):
        scoreFunc = np.vectorize(scoreFunc)
        return self.y * scoreFunc(self.x) * self.err

    def norm(self, xlims=None):
        """
        Normalize histogram area
        """
        vol = self.int(xlims=xlims)
        self.scaleY(1 / vol)
        return self

    def normPeak(self, showInterpPlot=False):
        peak = self.findMax(showInterpPlot=showInterpPlot)[1]
        #         peak  = np.max(self.y)
        self.scaleY(1 / peak)
        return self

    def normAtX(self, xInterpPoint, normAvgDomainRadius=1, kind="slinear"):
        if normAvgDomainRadius is None:
            interpPoints = [xInterpPoint]
        else:
            interpPoints = np.linspace(
                xInterpPoint - normAvgDomainRadius,
                xInterpPoint + normAvgDomainRadius,
                100,
            )

        yVal = np.average(self.interpTo(interpPoints, kind=kind).y)
        self.scaleY(1 / yVal)

        return self

    def peakNorm(self):
        peakPos, peakMax = self.findMax()
        self.scaleY(1.0 / peakMax)

    def int(self, xlims=None):
        """
        Return sum of histogram (value*bin_width)
        @param xlims: tuple of limits of integration (low,high)
        """

        total = 0.0

        ind = range(0, len(self.x))

        if xlims is not None:
            ind = self._getIndexInclusive(xlims[0], xlims[1])

        xRange = self.x[ind]
        yRange = self.y[ind]

        for i in range(0, len(xRange) - 1):
            binW = 1.0 * (xRange[i + 1] - xRange[i])
            midVal = (yRange[i + 1] + yRange[i]) / 2
            total += midVal * binW

        return total

    def findHalfArea(self):
        area = self.int()
        partialAreas = [self.int(xlims=(np.min(self.x), s)) for s in self.x]
        closestInd = np.argmin(np.abs(partialAreas - self.int() / 2))

        from scipy.interpolate import interp1d

        closestInterp = interp1d(
            partialAreas[closestInd - 3 : closestInd + 3],
            range(closestInd - 3, closestInd + 3),
            kind="cubic",
        )

        return closestInterp(area / 2) * (self.x[1] - self.x[0])

    def _getIndexInclusive(self, xlow, xhigh):
        return [
            s for s in range(0, len(self.x)) if self.x[s] >= xlow and self.x[s] <= xhigh
        ]

    def _avgDX(self, xlims=None):
        ind = range(0, len(self.x))

        if xlims is not None:
            ind = self._getIndexInclusive(xlims[0], xlims[1])

        toAv = self.x[ind]

        return np.average([toAv[s + 1] - toAv[s] for s in range(0, len(toAv) - 1)])

    def findY(self, yVal, guessList=None, interpType="cubic", showPlot=False):
        #         print "yVal: %s"%yVal
        #         print "maxFunc: %s"%np.max(self.y)

        intFunc = self.interp(
            kind=interpType, bounds_error=False, fill_value=np.finfo(np.float64).max
        )
        smoothFunc = np.vectorize(lambda x: intFunc(x) - yVal)

        if guessList is None:
            guessList = np.array([self.x[findNearestArrayVal(self.y, yVal)]])

        #
        from scipy.optimize import fsolve

        sol = fsolve(smoothFunc, guessList)

        if showPlot:
            xSpace = np.linspace(self.x[0], self.x[-1], 100)

            from matplotlib import pyplot as plt

            plt.plot(xSpace, intFunc(xSpace), "-")
            plt.plot(self.x, self.y, ".")
            #             plt.plot(sol, intFunc(sol), '.')
            plt.plot(xSpace, smoothFunc(xSpace))
            plt.text(
                0, 0, "yTarg: {}\nyVal: {}\nxVal{}".format(yVal, intFunc(sol), sol)
            )

            plt.show()

        return np.sort(sol)

    @classmethod
    def combine(cls, dataset1, dataset2):
        from scipy.interpolate import interp1d

        low1 = dataset1.x[0]
        high1 = dataset1.x[-1]
        low2 = dataset2.x[0]
        high2 = dataset2.x[-1]

        int1in2 = [
            s
            for s in range(0, len(dataset1.x))
            if (dataset1.x[s] >= low2 and dataset1.x[s] <= high2)
        ]
        int2in1 = [
            s
            for s in range(0, len(dataset2.x))
            if (dataset2.x[s] >= low1 and dataset2.x[s] <= high1)
        ]

        xint1 = dataset1.x[int1in2]
        xint2 = dataset2.x[int2in1]

        yint1 = dataset1.y[int1in2]
        yint2 = dataset2.y[int2in1]

        logging.info("X range of 1 intersecting 2: [{},{}]".format(xint1[0], xint1[-1]))
        logging.info("X range of 2 intersecting 1: [{},{}]".format(xint2[0], xint2[-1]))

        avDx1 = dataset1._avgDX((xint1[0], xint1[-1]))
        avDx2 = dataset2._avgDX((xint2[0], xint2[-1]))

        logging.info("AverageDX of 1 intersection: %s" % avDx1)
        logging.info("AverageDX of 2 intersection: %s" % avDx2)

        just1Ind = [s for s in range(0, len(dataset1.x)) if s not in int1in2]
        just2Ind = [s for s in range(0, len(dataset2.x)) if s not in int2in1]

        avgInty = []
        avgIntx = []

        if avDx1 < avDx2:
            f = interp1d(xint1, yint1, kind="cubic")
            intPoints = f(xint2)

            avgIntx = xint2
            avgInty = [(intPoints[s] + yint2[s]) / 2.0 for s in xint2]

            for ind, x in enumerate(xint1):
                if x not in avgIntx:
                    avgIntx = np.append(avgIntx, x)
                    avgInty = np.append(avgInty, avgInty[ind])

        elif avDx2 < avDx1:
            f = interp1d(xint2, yint2, kind="cubic")
            intPoints = f(xint1)

            avgIntx = xint1
            avgInty = [
                (intPoints[s] + yint1[s]) / 2.0 for s in range(0, len(intPoints))
            ]

            for ind, x in enumerate(xint2):
                if x not in avgIntx:
                    avgIntx = np.append(avgIntx, x)
                    avgInty = np.append(avgInty, yint2[ind])

        toRetx = np.concatenate([dataset1.x[just1Ind], dataset2.x[just2Ind], avgIntx])
        toRety = np.concatenate([dataset1.y[just1Ind], dataset2.y[just2Ind], avgInty])

        return DataSet1D(toRetx, toRety)

    def findMax(self, nIntPoints=3, showInterpPlot=False):
        """
        return function maximum determined from local inverse interpolation
        :param nIntPoints: number of local interpolation points
        :param showInterpPlot: show plot
        :return: xMax, yTargetMax
        """

        from scipy.interpolate import interp1d

        maxInd = np.argmax(self.y)
        #         print self.y
        #         print 'maxInd: ', maxInd
        #
        #         print len(self.x[maxInd-nIntPoints:maxInd+nIntPoints])
        #         print len(self.y[maxInd-nIntPoints:maxInd+nIntPoints])

        fitPeak = interp1d(
            self.x[maxInd - nIntPoints : maxInd + nIntPoints],
            self.y[maxInd - nIntPoints : maxInd + nIntPoints],
            kind="cubic",
        )

        max = findFuncMax(
            fitPeak,
            self.x[maxInd],
            self.x[maxInd - nIntPoints + 1],
            self.x[maxInd + nIntPoints - 1],
        )

        if showInterpPlot:
            from matplotlib import pyplot as plt

            interpX = np.linspace(
                self.x[maxInd - (nIntPoints - 1)],
                self.x[maxInd + (nIntPoints - 1)],
                100,
            )
            interpY = fitPeak(interpX)

            fig, ax = plt.subplots()
            ax.plot(
                self.x[maxInd - nIntPoints : maxInd + nIntPoints],
                self.y[maxInd - nIntPoints : maxInd + nIntPoints],
                ".b",
            )
            ax.plot(interpX, interpY, "--r")
            ax.text(0.05, 0.05, "peak=%s" % max, transform=ax.transAxes)

            plt.show()

        return (max, float(fitPeak(max)))

    def findPointBeyondMax(self, fractionOfMaxToLocate, nIntPoints=3):
        from scipy.interpolate import interp1d

        maxInd = np.argmax(self.y)
        maxX, maxY = self.findMax(nIntPoints)

        toSearchX = self.x[maxInd:-1]
        toSearchY = self.y[maxInd:-1]

        targetYVal = maxY * fractionOfMaxToLocate

        nearestInd = findNearestArrayVal(toSearchY, targetYVal)

        #         print targetYVal,nearestInd, toSearchY[nearestInd]
        #         print "max: %s"%maxInd
        #         print "nearest: %s"%nearestInd
        start, stop = nearestInd - nIntPoints, nearestInd + nIntPoints

        if start < 0:
            start = 0
        #         print "start, stop (%s,%s)"%(start,stop)

        #         print toSearchY, toSearchX
        z = zip(toSearchY[start:stop], toSearchX[start:stop])
        z = sorted(z)
        toSearchY, toSearchX = zip(*z)
        #         print np.array(toSearchX)
        #         print np.array(toSearchY)

        localFit = interp1d(toSearchY, toSearchX, kind="slinear")

        return float(localFit(targetYVal)), targetYVal

    def findPointBeforeMax(
        self, fractionOfMaxToLocate, nIntPoints=3, interpKind="linear"
    ):
        from scipy.interpolate import interp1d

        maxInd = np.argmax(self.y)
        maxX, maxY = self.findMax(nIntPoints)

        toSearchX = self.x[0:maxInd]
        toSearchY = self.y[0:maxInd]

        targetYVal = maxY * fractionOfMaxToLocate
        #         print "targ:",targetYVal
        #         print toSearchY
        #         print np.abs(toSearchY - targetYVal)

        nearestInd = findNearestArrayVal(toSearchY, targetYVal)

        #         print targetYVal,nearestInd, toSearchY[nearestInd]
        #         print "max: %s"%maxInd
        #         print "nearest: %s"%nearestInd
        start, stop = nearestInd - nIntPoints, nearestInd + nIntPoints

        if start < 0:
            start = 0
        #         print "start, stop (%s,%s)"%(start,stop)

        #         print toSearchY, toSearchX
        z = zip(toSearchY[start:stop], toSearchX[start:stop])
        z = sorted(z)
        toSearchY, toSearchX = zip(*z)
        #         print np.array(toSearchX)
        #         print np.array(toSearchY)

        localFit = interp1d(toSearchY, toSearchX, kind=interpKind)

        #         print localFit(targetYVal)

        return float(localFit(targetYVal)), targetYVal

    def fastFindY(self, yval):
        pass

    def writeCsv(self, fname, *arr_tup_csv_args, **arr_tup_csv_kwargs):
        if self.err is None:
            array_tuple_to_csv(
                fname, (self.x, self.y), *arr_tup_csv_args, **arr_tup_csv_kwargs
            )
        else:
            array_tuple_to_csv(
                fname,
                (self.x, self.y, self.err),
                *arr_tup_csv_args,
                **arr_tup_csv_kwargs,
            )

    def interp(self, *args, **kwargs):
        from scipy.interpolate import interp1d

        return interp1d(self.x, self.y, *args, **kwargs)

    def interpTo(self, xValueList, **interp1d_kwargs):
        from scipy.interpolate import interp1d

        if "kind" not in interp1d_kwargs.keys():
            interp1d_kwargs["kind"] = "slinear"

        f = interp1d(self.x, self.y, **interp1d_kwargs)

        if self.err is not None:
            e = interp1d(self.x, self.err, **interp1d_kwargs)
            return DataSet1D(xValueList, f(xValueList), err=e(xValueList))
        else:
            return DataSet1D(xValueList, f(xValueList))

    def averageY(self, midPointx, numPoints):
        xMidInd = np.argmin(np.abs(self.x - midPointx))
        return np.average(self.y[xMidInd - numPoints : xMidInd + numPoints])

    def plot(self, ax=None, fmt=None, *args, **kwargs):
        from matplotlib import pyplot as plt

        ax = ax or plt.gca()

        if fmt is None:
            p = ax.plot(self.x, self.y, *args, **kwargs)
        else:
            p = ax.plot(self.x, self.y, fmt, *args, **kwargs)

        return p

    def errorbar(self, ax, *args, **kwargs):
        kwargs["yerr"] = self.absError

        return ax.errorbar(self.x, self.y, *args, **kwargs)

    def convolveDiscreet(self, convolutionFunction, convFunctionError=0):
        """
        convolve dataset (sum, multiplied by function(x))
        :param convolutionFunction: function of x to multiply bin-wise
        :param confFunctionError: universal % error 0 < convFunctionError < 1
        """
        assert 0 <= convFunctionError <= 1

        toRet = 0
        sqErr = 0
        for ind, xval in enumerate(self.x):
            #             yval = ufloat((self.y[ind], self.absError[ind]))
            #             cfv = convolutionFunction(xval)
            #             cfv = ufloat((cfv, convFunctionError*cfv))
            #

            yval = self.y[ind]
            cfv = convolutionFunction(xval)

            val = yval * cfv
            err = np.sqrt(self.err[ind] ** 2 + convFunctionError**2) * val

            toRet += val
            sqErr += err**2

        #         print "%s %s (%s)"%(toRet, np.sqrt(sqErr),np.sqrt(sqErr)/toRet)

        return ufloat(toRet, np.sqrt(sqErr))

    def calcAverageError(self):
        nonZeroSet = np.nonzero(self.y)[0]

        #         print 'non zero set', nonZeroSet
        sumNonZero = np.sum(self.y[nonZeroSet])

        #         print 'non zero sum', sumNonZero

        # error weighted by data values

        toRetSum = 0
        if len(nonZeroSet) > 0:
            toRetSum = (
                np.sum([self.y[s] * self.err[s] for s in nonZeroSet]) / sumNonZero
            )

        return toRetSum

    def fitLinear(self):
        """
        return: linear function fit to data
        """
        from scipy.stats import linregress

        slope, intercept, r_value, p_value, std_err = linregress(self.x, self.y)

        logging.info(
            "Linear fit of DataSet1D: m=%s,b=%s,std_err=%s"
            % (slope, intercept, std_err)
        )

        return np.vectorize(lambda x: intercept + slope * x)

    def getNearestXArg(self, xval, underCut=False):
        if not underCut:
            return np.argmin(np.abs(self.x - xval))
        else:
            min = np.argmin(np.abs(self.x - xval))
            if self.x[min] > xval:
                return min - 1
            else:
                return min

    def getNearestYArg(self, yVal):
        return np.argmin(np.abs(self.y - yVal))

    def getNearestX(self, yval, dataSlice=None):
        if dataSlice is None:
            dataSlice = (self.x[0], self.x[-1])

        dSpace = slice(
            self.getNearestXArg(dataSlice[0]), self.getNearestXArg(dataSlice[1])
        )

        return self.x[dSpace][np.argmin(np.abs(self.y[dSpace] - yval))]

    def slice(self, sliceValList):
        assert isinstance(sliceValList, list) or isinstance(sliceValList, int)

        if isinstance(sliceValList, int):
            sliceValList = [sliceValList]

        for s in sliceValList:
            if not isinstance(s, int):
                raise RuntimeError("only integer indeces allowed")
            if not s <= len(self.x):
                raise RuntimeError(
                    "slice index ({}) larger than list length ({})".format(
                        s, len(self.x)
                    )
                )

        sliceValList.sort()
        svl = sliceValList

        slices = [slice(svl[s], svl[s + 1]) for s in range(0, len(svl) - 1)]

        return [slice(0, svl[0])] + slices + [slice(svl[-1], len(self.x) + 1)]

    def concat(self, ds1d_list):
        if isinstance(ds1d_list, DataSet1D):
            ds1d_list = [ds1d_list]

        x = self.x
        y = self.y
        if self.err is not None:
            err = self.err
        else:
            err = None

        for ds in ds1d_list:
            assert isinstance(ds, DataSet1D)
            assert len(np.intersect1d(x, ds.x)) == 0

            x = np.concatenate((x, ds.x))
            y = np.concatenate((y, ds.y))

            if err is not None:
                err = np.concatenate((err, ds.err))

        return DataSet1D(x, y, err)
