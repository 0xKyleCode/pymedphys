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
import abc

from tkinter import messagebox
from matplotlib import pyplot as plt
import matplotlib as mpl
import tkinter as tk

import numpy as np
from matplotlib.backend_tools import ToolBase
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from matplotlib.widgets import (
    EllipseSelector,
    SpanSelector,
    AxesWidget,
    Slider,
    RectangleSelector,
)

from pyvic.util.data_structures import NDVoxelArray
from pyvic.util.file import DataFrameableCollectable, InfoFile
from pyvic.util.utils import flatten_tuple_list
from pyvic.util.image import circular_mask


class VoxelScrollerFigure:
    AXISCOL = ["g", "y", "r"]

    def __init__(self, vox_array, vmin=None, vmax=None, title=None, **imshow_kwargs):
        """

        :type vox_array: NDVoxelArray
        """
        self.shape = np.shape(vox_array)
        self.fig, self.axes = plt.subplots(2, 2)
        self.axes = self.axes.flatten()
        self._axDict = {self.axes[0]: 0, self.axes[1]: 1, self.axes[2]: 2}
        self.vox_array = vox_array

        self.vmin = vmin or np.min(vox_array)
        self.vmax = vmax or np.max(vox_array)

        self.slice_pos = [int(s / 2.0) for s in self.shape]

        self.plotter = NDVoxelPlotter(vox_array)
        self.lines = [
            None,
        ] * 3
        self.img = [
            None,
        ] * 3
        self.init()

        self.fig.canvas.mpl_connect("scroll_event", self.scroll)

        mng = plt.get_current_fig_manager()
        ### works on Ubuntu??? >> did NOT working on windows
        mng.resize(*mng.window.maxsize())
        # mng.window.state('zoomed')  # works fine on Windows!

        if title is not None:
            plt.title(title)

        plt.show()

    def init(self):
        for i in range(0, 3):
            self.updateImage(i)

            for spine in self.axes[i].spines.values():
                spine.set_edgecolor(self.AXISCOL[i])
                spine.set_linewidth(5)

            dim_list = self.plotter._get_dim_list([i])

            self.axes[i].set_ylabel(
                NDVoxelArray.AXIS_NAMES[dim_list[0]], color=self.AXISCOL[dim_list[0]]
            )

            self.axes[i].set_xlabel(
                NDVoxelArray.AXIS_NAMES[dim_list[1]], color=self.AXISCOL[dim_list[1]]
            )

        self.updateGuideLines()

    def scroll(self, event):
        if event.inaxes is not None:
            an = self._axDict[event.inaxes]

            nextSlice = list(self.slice_pos)
            nextSlice[an] = nextSlice[an] + event.step

            if nextSlice[an] >= 0 and nextSlice[an] < self.shape[an]:
                self.setSlicePos(tuple(nextSlice))

    def setSlicePos(self, pos):
        oldPos = self.slice_pos
        self.slice_pos = pos

        for ind, diff in enumerate(np.array(oldPos) - np.array(self.slice_pos)):
            if diff != 0:
                self.updateImage(ind)
                self.updateGuideLines()

    def updateGuideLines(self):
        for ind in range(0, 3):
            ax = self.axes[ind]

            lineAxes = list(range(0, 3))
            lineAxes.pop(ind)
            verAx, horAx = lineAxes[0], lineAxes[1]

            slc_indices = self.slice_pos

            slc_coords = self.vox_array.index_tuple_to_coord(self.slice_pos)

            if self.lines[ind] is None:
                self.lines[ind] = (
                    self.plotter.plot_vertical_line(
                        self.axes[ind],
                        ind,
                        horizontal_coord=slc_coords[horAx],
                        ls="--",
                        color=self.AXISCOL[horAx],
                    ),
                    self.plotter.plot_horizontal_line(
                        self.axes[ind],
                        ind,
                        vertical_coord=slc_coords[verAx],
                        ls="--",
                        color=self.AXISCOL[verAx],
                    ),
                )
            else:
                self.lines[ind][0].set_xdata((slc_coords[horAx], slc_coords[horAx]))
                self.lines[ind][1].set_ydata((slc_coords[verAx], slc_coords[verAx]))

    def updateImage(self, imgNum):
        ax = self.axes[imgNum]
        ax_name = NDVoxelArray.AXIS_NAMES[imgNum]
        slice_num = self.slice_pos[imgNum]

        if self.img[imgNum] is None:
            self.img[imgNum] = self.plotter.plot_slice(
                ax,
                [(imgNum, slice_num)],
                vmin=self.vmin,
                vmax=self.vmax,
                cmap="Greys_r",
            )
        else:
            slc = self.plotter._get_slice_index([(imgNum, slice_num)])
            self.img[imgNum].set_data(self.vox_array[slc])

        ax.set_title("{} slice: {}".format(ax_name, slice_num))
        ax.figure.canvas.draw()

    def updateAllImages(self):
        for i in range(0, 3):
            self.updateImage(i)


class NDScrollPlotter:
    def __init__(self, image_set, vmin=None, vmax=None, **mpl_imshow_args):
        self.n_images = len(image_set)
        self.shape = np.shape(image_set[0])

        assert np.all([np.shape(s) == np.shape(image_set[0]) for s in image_set])

        self.fig, self.ax = plt.subplots()

        self.image_set = NDVoxelArray(np.dstack(image_set))
        self.cur_image = None

        self.vmin = vmin or np.min(image_set)
        self.vmax = vmax or np.max(image_set)

        self.slice_pos = 0
        self.plotter = NDVoxelPlotter(self.image_set)

        self.updateImage()

        # self.fig.canvas.mpl_connect('scroll_event', self.scroll)
        pass

    def updateImage(self):
        ax = self.ax

        if self.cur_image is None:
            self.cur_image = self.plotter.plot_x_slice(
                ax, self.slice_pos, vmin=self.vmin, vmax=self.vmax, cmap="Greys_r"
            )
        else:
            self.cur_image.set_data(self.image_set[:, :, self.slice_pos])

        ax.figure.canvas.draw()


class NDVoxelPlotter:
    def __init__(self, nd_voxel_obj, mask=None, edge_padded=False):
        """

        :type nd_voxel_obj: pydose.utils.data_structures.NDVoxelArray
        """
        self.edge_padded = edge_padded

        # if mask is written as np.where...
        if isinstance(mask, tuple) and len(mask) == 2:
            masked_array = np.zeros_like(nd_voxel_obj)
            masked_array[mask] = True
            self.mask = masked_array
            assert np.shape(self.mask) == np.shape(nd_voxel_obj)
        elif np.shape(mask) == np.shape(nd_voxel_obj):
            self.mask = mask
        elif mask is None:
            self.mask = None
        else:
            raise NotImplementedError()

        if len(nd_voxel_obj.shape) == 2:
            # print 'orig:',np.shape(nd_voxel_obj), nd_voxel_obj.__class__, nd_voxel_obj.origin, nd_voxel_obj.voxdims
            new_arr_view = nd_voxel_obj[np.newaxis, :, :]
            self.voxel_array = NDVoxelArray(
                new_arr_view,
                voxdims=(1, nd_voxel_obj.voxdims[0], nd_voxel_obj.voxdims[1]),
                origin=(0, nd_voxel_obj.origin[0], nd_voxel_obj.origin[1]),
            )
            # print 'new:',np.shape(self.voxel_array), self.voxel_array.__class__,self.voxel_array.origin, self.voxel_array.voxdims
        else:
            self.voxel_array = nd_voxel_obj
        self._vox_min = np.min([s[0] for s in self.voxel_array.bounds])
        self._vox_max = np.max([s[1] for s in self.voxel_array.bounds])

    def plot_slice(self, ax, slice_index_tuple=[], **mpl_plot_kwargs):
        nd_vox_dimension = len(self.voxel_array.shape)

        assert len(slice_index_tuple) == nd_vox_dimension - 2

        # 2D, plot slice
        if len(self.voxel_array.shape) == 2:
            data = self.voxel_array
            import copy

            bounds = copy.copy(self.voxel_array.bounds)
            bounds.reverse()
            bounds = flatten_tuple_list(bounds)
            dim_list = [1, 2]

        # 3D, plot slice with coord
        elif len(self.voxel_array.shape) == 3:
            slc = self._get_slice_index(slice_index_tuple)

            excluded_dims = [s[0] for s in slice_index_tuple]
            dim_list = self._get_dim_list(excluded_dims)
            data = self.voxel_array[tuple(slc)]

            bounds = flatten_tuple_list(
                reversed([self.voxel_array.bounds[i] for i in dim_list])
            )

        else:
            raise NotImplementedError()

        if self.mask is not None:
            data = np.ma.masked_array(data, self.mask)

        plt = ax.imshow(
            data, origin="lower", extent=bounds, interpolation="None", **mpl_plot_kwargs
        )
        ax.set_xlabel(NDVoxelArray.AXIS_NAMES[dim_list[1]])
        ax.set_ylabel(NDVoxelArray.AXIS_NAMES[dim_list[0]])

        return plt

    def _get_dim_list(self, excluded_dims):
        dim_list = list(range(0, len(self.voxel_array.shape)))
        for dim in excluded_dims:
            dim_list.remove(dim)
        return dim_list

    def _get_slice_index(self, dim_coordIndex_tuplelist):
        slc = [
            slice(None),
        ] * len(self.voxel_array.shape)

        for dim_number, coord_index in dim_coordIndex_tuplelist:
            assert dim_number < len(self.voxel_array.shape)

            assert coord_index < self.voxel_array.shape[dim_number] and coord_index >= 0

            slc[dim_number] = coord_index

        return slc

    def plot_x_slice(self, ax, x_index, **mpl_plot_kwargs):
        return self.plot_slice(ax, [(NDVoxelArray.XAXIS, x_index)], **mpl_plot_kwargs)

    def plot_y_slice(self, ax, y_index, **mpl_plot_kwargs):
        return self.plot_slice(ax, [(NDVoxelArray.YAXIS, y_index)], **mpl_plot_kwargs)

    def plot_z_slice(self, ax, z_index, **mpl_plot_kwargs):
        return self.plot_slice(ax, [(NDVoxelArray.ZAXIS, z_index)], **mpl_plot_kwargs)

    def plot_point(
        self, ax, plane_dimension, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
    ):
        assert len(zyx_point_coords) == len(self.voxel_array.shape)
        dim_list = self._get_dim_list([plane_dimension])
        hor_point, ver_point = (
            zyx_point_coords[dim_list[1]],
            zyx_point_coords[dim_list[0]],
        )
        ax.plot([hor_point], [ver_point], *mpl_plot_args, **mpl_plot_kwargs)

    def plot_point_zplane(
        self, ax, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
    ):
        return self.plot_point(
            ax, NDVoxelArray.ZAXIS, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
        )

    def plot_point_yplane(
        self, ax, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
    ):
        return self.plot_point(
            ax, NDVoxelArray.YAXIS, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
        )

    def plot_point_xplane(
        self, ax, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
    ):
        return self.plot_point(
            ax, NDVoxelArray.XAXIS, zyx_point_coords, *mpl_plot_args, **mpl_plot_kwargs
        )

    def plot_line(
        self, ax, plane_dimension, zyx_line_1=None, zyx_line_2=None, **mpl_plot_kwargs
    ):
        dim_list = self._get_dim_list([plane_dimension])

        ax_dim_x, ax_dim_y = self._get_ax_lims(ax)

        hor_point1, ver_point1 = zyx_line_1[dim_list[1]], zyx_line_1[dim_list[0]]
        hor_point2, ver_point2 = zyx_line_2[dim_list[1]], zyx_line_2[dim_list[0]]

        # print hor_point1, hor_point2
        # print ver_point1, ver_point2

        toRet = ax.plot(
            [hor_point1, hor_point2], [ver_point1, ver_point2], **mpl_plot_kwargs
        )

        self._set_ax_lims(ax, ax_dim_x, ax_dim_y)
        return toRet[0]

    def plot_vertical_line(
        self, ax, plane_dimension, horizontal_coord=None, **mpl_plot_kwargs
    ):
        x_lim, y_lim = self._get_ax_lims(ax)

        dim_list = self._get_dim_list([plane_dimension])

        if horizontal_coord is None:
            horizontal_coord = (x_lim[1] + x_lim[0]) / 2.0

        zyx_1 = [None] * 3
        zyx_1[dim_list[1]] = horizontal_coord
        zyx_1[dim_list[0]] = y_lim[0]
        zyx_1[plane_dimension] = 0

        zyx_2 = [None] * 3
        zyx_2[dim_list[1]] = horizontal_coord
        zyx_2[dim_list[0]] = y_lim[1]
        zyx_2[plane_dimension] = 0

        return self.plot_line(ax, plane_dimension, zyx_1, zyx_2, **mpl_plot_kwargs)

    def plot_horizontal_line(
        self, ax, plane_dimension, vertical_coord=None, **mpl_plot_kwargs
    ):
        x_lim, y_lim = self._get_ax_lims(ax)

        dim_list = self._get_dim_list([plane_dimension])

        if vertical_coord is None:
            vertical_coord = (y_lim[1] + y_lim[0]) / 2.0

        zyx_1 = [None] * 3
        zyx_1[dim_list[1]] = x_lim[0]
        zyx_1[dim_list[0]] = vertical_coord
        zyx_1[plane_dimension] = 0

        zyx_2 = [None] * 3
        zyx_2[dim_list[1]] = x_lim[1]
        zyx_2[dim_list[0]] = vertical_coord
        zyx_2[plane_dimension] = 0

        return self.plot_line(ax, plane_dimension, zyx_1, zyx_2, **mpl_plot_kwargs)

    def plot_box(
        self, ax, plane_dimension, top_left_coord, bottom_right_coord, **mpl_plot_kwargs
    ):
        self.plot_vertical_line(
            ax, plane_dimension, top_left_coord[1], **mpl_plot_kwargs
        )
        self.plot_vertical_line(
            ax, plane_dimension, bottom_right_coord[1], **mpl_plot_kwargs
        )
        self.plot_horizontal_line(
            ax, plane_dimension, top_left_coord[0], **mpl_plot_kwargs
        )
        self.plot_horizontal_line(
            ax, plane_dimension, bottom_right_coord[0], **mpl_plot_kwargs
        )

    def plot_voxel_hist(self, ax, *mpl_hist_args, **mpl_hist_kwargs):
        ax.hist(self.voxel_array.flatten(), *mpl_hist_args, **mpl_hist_kwargs)

        pass

    @classmethod
    def _get_ax_lims(cls, ax):
        return ax.get_xlim(), ax.get_ylim()

    @classmethod
    def _set_ax_lims(cls, ax, x_lim, y_lim):
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)

    # def plot_profile(self, ax, profile_dimension, , **mpl_plot_kwargs):
    #     x_lim, y_lim = self._get_ax_lims(ax)
    #
    #     dim_list = self._get_dim_list([plane_dimension])
    #
    #     if vertical_coord is None:
    #         vertical_coord = (y_lim[1] + y_lim[0]) / 2.0
    #
    #     zyx_1 = [None] * 3
    #     zyx_1[dim_list[1]] = x_lim[0]
    #     zyx_1[dim_list[0]] = vertical_coord
    #     zyx_1[plane_dimension] = 0
    #
    #     zyx_2 = [None] * 3
    #     zyx_2[dim_list[1]] = x_lim[1]
    #     zyx_2[dim_list[0]] = vertical_coord
    #     zyx_2[plane_dimension] = 0
    #
    #     return self.plot_line(ax, plane_dimension, zyx_1, zyx_2, **mpl_plot_kwargs)


def histogram_bins_peaks(data, *np_hist_args, **np_hist_kwargs):
    y, binEdges = np.histogram(data, *np_hist_args, **np_hist_kwargs)
    bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
    return bincenters, y


def plot_hist_bins(ax, data, bins, normed, *plt_args, **plt_kwargs):
    x, y = histogram_bins_peaks(data, bins, normed=normed)
    return ax.plot(x, y, *plt_args, **plt_kwargs)


class EllipseTool(ToolBase):
    import os

    image = os.path.join("..", "assets", "ellipse_icon.png")


class ROISelectorToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas_, parent_, app):
        self.app = app

        self._rect = app.enable_rect
        self._ellipse = app.enable_ellipse

        self.toolitems = (
            ("Home", "Home", "home", "home"),
            ("Back", "Back", "back", "back"),
            ("Forward", "Forward", "forward", "forward"),
            (None, None, None, None),
            ("Pan", "Pan", "move", "pan"),
            ("Zoom", "Zoom", "zoom_to_rect", "zoom"),
            (None, None, None, None),
            ("Save", "Save", "filesave", "save_figure"),
            ("Ellipse", "Ellipse", "hand", "_ellipse"),
            ("Rectangle", "Rectangle", "hand", "_rect"),
        )
        NavigationToolbar2Tk.__init__(self, canvas_, parent_)


class ROISelectorWindow:
    def __init__(self, img, root=None, roi_file=None, *plt_args, **plt_kwargs):
        if root is None:
            import tkinter as tk

            root = tk.Tk()

        self.root = root
        self._init_app()

        self.img = img
        self.plot(self.img, *plt_args, **plt_kwargs)

        self.e_selector = EllipseSelector(self.ax, self.draw_ellipse, drawtype="line")
        self.e_selector.set_active(False)

        self.r_selector = RectangleSelector(self.ax, self.draw_rectangle)
        self.r_selector.set_active(False)

        self.rois = []
        self.root.protocol("WM_DELETE_WINDOW", self.closing)

        import os

        self.roi_file = roi_file

        if self.roi_file is not None and os.path.isfile(self.roi_file):
            roi_dict = RegionOfInterest.from_dataframe(self.roi_file)

            for name, roi in roi_dict.iteritems():
                self.add_roi(roi)

        self.root.mainloop()

        # test.ax.connect('key_press_event', toggle_selector)

    def closing(self):
        if self.roi_file is not None:
            if messagebox.askyesno(
                "Save ROI", "Do you want to save ROIs to file %s?" % self.roi_file
            ):
                print("saving ROI's to %s" % (self.roi_file))
                df = RegionOfInterest.to_dataframe(self.rois)
                df.to_pickle(self.roi_file)
        self.root.destroy()

    # here we embed the a figure in the Tk GUI
    def _init_app(self):
        self.figure = mpl.figure.Figure()
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)

        self.toolbar = ROISelectorToolbar(self.canvas, self.root, self)
        self.toolbar.update()
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        # self.canvas.draw()

    # plot something random
    def plot(self, img, *imshow_args, **imshow_kwargs):
        imshow_kwargs["origin"] = "lower"

        if "cmap" not in imshow_kwargs.keys():
            imshow_kwargs["cmap"] = "Greys_r"

        self.ax.imshow(img, *imshow_args, **imshow_kwargs)
        self.figure.canvas.draw()

    def enable_ellipse(self):
        self.r_selector.visible = False
        self.r_selector.set_active(False)

        self.e_selector.visible = True
        self.e_selector.set_active(True)

    def enable_rect(self):
        self.e_selector.visible = False
        self.e_selector.set_active(False)

        self.r_selector.visible = True
        self.r_selector.set_active(True)

    def draw_ellipse(self, start, stop):
        self.e_selector.visible = False
        self.e_selector.set_active(False)

        x0, y0 = start.xdata, start.ydata
        x1, y1 = stop.xdata, stop.ydata

        mid = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = np.abs(x0 - x1), np.abs(y0 - y1)

        e = EllipseROI.create_named(self.root, mid, dx, dy, img_size=np.shape(self.img))

        self.add_roi(e)

    def draw_rectangle(self, start, stop):
        self.e_selector.visible = False
        self.e_selector.set_active(False)

        x0, y0 = start.xdata, start.ydata
        x1, y1 = stop.xdata, stop.ydata

        mid = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = np.abs(x0 - x1), np.abs(y0 - y1)

        # e = EllipseROI.create_named(self.root, mid, dx, dy, img_size=np.shape(self.img))
        self.r_selector.set_active(False)
        r = RectangleROI.create_named(
            self.root, mid, dx, dy, img_size=np.shape(self.img)
        )
        self.add_roi(r)
        self.r_selector.set_active(True)

    def _add_new(self, s, evt):
        ell = EllipseROI.create_named(
            self.root,
            (s.mid[0] + 0.25 * s.width, s.mid[1] + 0.25 * s.height),
            s.width,
            s.height,
            img_size=np.shape(self.img),
        )
        if ell is not None:
            self.add_roi(ell)

    def _delete(self, s, evt):
        self.remove_roi(s)

    def add_roi(self, roi):
        roi.add_double_click_event(self._add_new)
        roi.add_rclick(self._delete)
        self.ax.add_artist(roi.get_artist())
        self.ax.add_artist(roi.text_artist)
        self.rois.append(roi)
        roi.artist.figure.canvas.draw()
        roi.connect()
        print(roi)

    def remove_roi(self, roi):
        assert roi in self.rois
        roi.artist.set_visible(False)
        roi.text_artist.set_visible(False)
        self.figure.canvas.draw()
        self.rois.remove(roi)
        roi.disconnect()

        del roi

    def onselect(eclick, erelease):
        "eclick and erelease are matplotlib events at press and release"

        print(" used button   : ", eclick.button)
        pass
        # print(' startposition : (%f, %f)' % (eclick.xdata, eclick.ydata))
        # print(' endposition   : (%f, %f)' % (erelease.xdata, erelease.ydata))

        # def toggle_selector(event):
        #     print(' Key pressed.')
        #     if event.key in ['Q', 'q'] and toggle_selector.ES.active:
        #         print(' EllipseSelector deactivated.')
        #         toggle_selector.RS.set_active(False)
        #     if event.key in ['A', 'a'] and not toggle_selector.ES.active:
        #         print(' EllipseSelector activated.')
        #         toggle_selector.ES.set_active(True)


class ROISingleSelectWindow(ROISelectorWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.r_selector.set_active(True)

    def draw_rectangle(self, start, stop):
        self.e_selector.visible = False
        self.e_selector.set_active(False)

        x0, y0 = start.xdata, start.ydata
        x1, y1 = stop.xdata, stop.ydata

        mid = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = np.abs(x0 - x1), np.abs(y0 - y1)

        # e = EllipseROI.create_named(self.root, mid, dx, dy, img_size=np.shape(self.img))
        self.r_selector.set_active(False)
        r = RectangleROI(mid, dx, dy, img_size=np.shape(self.img))
        print(r.slice_literal())
        self.root.quit()

        # self.r_selector.set_active(True)

    pass


class RegionOfInterest(DataFrameableCollectable):
    __metaclass__ = abc.ABCMeta

    def __init__(self, mid, width, height, text=None, img_size=None):
        self.artist = None

        self.mid = mid
        self.width = width
        self.height = height

        self.press = None

        if text is not None:
            self.text = text
            from matplotlib.text import Text

            self.text_artist = Text(x=mid[0], y=mid[1], text=text)
        else:
            self.text = text
            self.text_artist = None

        self.double_click_event = None
        self.right_click_event = None
        self.release_event = None

        self.image_size = img_size

    def to_dataframe_dict(self):
        return {
            "mid": self.mid,
            "width": self.width,
            "height": self.height,
            "text": self.text,
            "img_size": self.image_size,
            "class": self.__class__,
        }

    @classmethod
    def from_dataframe_dict(cls, df_dict):
        return df_dict["class"](
            df_dict["mid"],
            df_dict["width"],
            df_dict["height"],
            df_dict["text"],
            df_dict["img_size"],
        )

    def add_release_event(self, func):
        self.release_event = func

    def add_double_click_event(self, func):
        self.double_click_event = func

    def add_rclick(self, func):
        self.right_click_event = func

    def get_artist(self, *artist_args, **artist_kwargs):
        self.artist = self.roi_artist(*artist_args, **artist_kwargs)
        return self.artist

    @abc.abstractproperty
    def roi_artist(self, *artist_args, **artist_kwargs):
        pass

    def connect(self):
        "connect to all the events we need"
        self.cidpress = self.artist.figure.canvas.mpl_connect(
            "button_press_event", self.on_press
        )
        self.cidrelease = self.artist.figure.canvas.mpl_connect(
            "button_release_event", self.on_release
        )
        self.cidmotion = self.artist.figure.canvas.mpl_connect(
            "motion_notify_event", self.on_motion
        )

    def on_press(self, event):
        "on button press we will see if the mouse is over us and store some data"
        if event.inaxes != self.artist.axes:
            return

        contains, attrd = self.artist.contains(event)
        if not contains:
            return

        try:
            x0, y0 = self.artist.center
        except AttributeError:
            x0, y0 = (
                self.artist.xy[0] + self.artist.get_width() / 2.0,
                self.artist.xy[1] + self.artist.get_height() / 2.0,
            )

        if event.button == 1:
            if event.dblclick:
                if self.double_click_event is not None:
                    self.double_click_event(self, event)
            else:
                self.press = x0, y0, event.xdata, event.ydata
        elif event.button == 3:
            if self.right_click_event is not None:
                self.right_click_event(self, event)

    def on_motion(self, event):
        "on motion we will move the rect if the mouse is over us"
        if self.press is None:
            return
        if event.inaxes != self.artist.axes:
            return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        # print('x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f' %
        #      (x0, xpress, event.xdata, dx, x0+dx))

        if isinstance(self.artist, Rectangle):
            self.artist.set_x(x0 - (self.artist.get_width() / 2.0) + dx)
            self.artist.set_y(y0 - (self.artist.get_height() / 2.0) + dy)
        else:
            self.artist.center = x0 + dx, y0 + dy

        if self.text_artist is not None:
            self.text_artist.set_x(x0 + dx)
            self.text_artist.set_y(y0 + dy)

        self.mid = x0 + dx, y0 + dy

        self.artist.figure.canvas.draw()

    def on_release(self, event):
        "on release we reset the press data"

        if self.release_event is not None:
            self.release_event(event)

        self.press = None
        self.artist.figure.canvas.draw()

    def disconnect(self):
        "disconnect all the stored connection ids"
        self.artist.figure.canvas.mpl_disconnect(self.cidpress)
        self.artist.figure.canvas.mpl_disconnect(self.cidrelease)
        self.artist.figure.canvas.mpl_disconnect(self.cidmotion)

    @classmethod
    def create_named(cls, root, *args, **kwargs):
        w = popupWindow(root)
        root.wait_window(w.top)

        try:
            kwargs["text"] = w.value
        except AttributeError:
            return None

        return cls(*args, **kwargs)

    def mask(self):
        mask = np.zeros(self.image_size)

        lx, hx = int(round(self.mid[0] - self.width / 2.0)), int(
            round(self.mid[0] + self.width / 2.0)
        )
        ly, hy = int(round(self.mid[1] - self.height / 2.0)), int(
            round(self.mid[1] + self.height / 2.0)
        )

        mask[ly : hy + 1, lx : hx + 1] = 1
        return mask

    def mask_as_index(self):
        return np.where(self.mask() == 1)

    def slice_literal(self):
        lx, hx = int(round(self.mid[0] - self.width / 2.0)), int(
            round(self.mid[0] + self.width / 2.0)
        )
        ly, hy = int(round(self.mid[1] - self.height / 2.0)), int(
            round(self.mid[1] + self.height / 2.0)
        )

        return slice(ly, hy, None), slice(lx, hx)
        # mask[ly:hy + 1, lx:hx + 1] = 1
        # return mask

    def __str__(self):
        return "{},{} ({},{})".format(self.mid[0], self.mid[1], self.width, self.height)

    @classmethod
    def from_dataframe(cls, df_file):
        # type: (str) -> dict[str,RegionOfInterest]

        list, md = super().from_dataframe(df_file)
        return {s.text: s for s in list}


class popupWindow:
    def __init__(self, master):
        import tkinter as tk

        top = self.top = tk.Toplevel(master)
        self.l = tk.Label(top, text="ROI Name")
        self.l.pack()
        self.e = tk.Entry(top)
        self.e.pack()
        self.b = tk.Button(top, text="Ok", command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()


class EllipseROI(RegionOfInterest):
    def roi_artist(self, *artist_args, **artist_kwargs):
        from matplotlib.patches import Ellipse

        return Ellipse(
            xy=self.mid,
            width=self.width,
            height=self.height,
            *artist_args,
            **artist_kwargs
        )

    def mask(self):
        return circular_mask(
            self.image_size,
            (self.mid[1], self.mid[0]),
            np.max([self.width / 2.0, self.height / 2.0]),
        )


class RectangleROI(RegionOfInterest):
    def roi_artist(self, *artist_args, **artist_kwargs):
        from matplotlib.patches import Rectangle

        return Rectangle(
            xy=(self.mid[0] - self.width / 2.0, self.mid[1] - self.height / 2.0),
            width=self.width,
            height=self.height,
            *artist_args,
            **artist_kwargs
        )

    def mask(self):
        return None
        # return circular_mask(self.image_size, (self.mid[1], self.mid[0]), np.max([self.width / 2.0, self.height / 2.0]))


class PlotScroller:
    __metaclass__ = abc.ABCMeta

    def __init__(self, data_sets, data_fmts=None, names=None, figure=None, axes=None):
        self.data_sets = data_sets
        self.num_data = len(data_sets[0])
        self.cur_set = 0

        if data_fmts is None:
            self.fmts = ["-" for s in data_sets]
        else:
            assert len(data_fmts) == len(data_sets)
            self.fmts = data_fmts

        if names is not None:
            assert len(names) == len(data_sets)
            self.names = names
        else:
            self.names = [None] * len(data_sets)
        from matplotlib import gridspec

        gs = gridspec.GridSpec(2, 1, height_ratios=[0.95, 0.05])

        self.fig = plt.figure()

        # initialize plots
        self.data_ax = self.fig.add_subplot(gs[0])
        self.data_plots = None

        self.plot_init()

        # inti scroll event
        self._scroll_event_count = 0
        self.fig.canvas.mpl_connect("scroll_event", self.mouse_scroll)

        # initialize slider
        self.slide_ax = self.fig.add_subplot(gs[1])
        self.slc_slider = Slider(
            self.slide_ax, "slice", 0, self.num_data - 1, valinit=0, valfmt="%d"
        )
        self.slc_slider.on_changed(self.slider_update)

        self.update()

    # initialize plots, return plot handles
    @abc.abstractmethod
    def plot_init(self):
        pass

    # initialize plots, return plot handles
    @abc.abstractmethod
    def update_plots(self, plot_num):
        pass

    def update(self):
        self.update_plots(self.cur_set)
        self.slc_slider.set_val(self.cur_set)
        self.fig.canvas.draw_idle()

    def scroll_update(self, set_num):
        if self.cur_set != set_num and self._scroll_event_count == 0:
            self._scroll_event_count += 1

            self.cur_set = set_num

            if self.cur_set < 0:
                self.cur_set = 0
            elif self.cur_set >= self.num_data:
                self.cur_set = self.num_data - 1

            self.update()

            self._scroll_event_count -= 1

    def mouse_scroll(self, event):
        if event.inaxes is not None and event.inaxes == self.data_ax:
            self.scroll_update(self.cur_set + event.step)

    def slider_update(self, slider_val):
        slider_val = int(np.ceil(slider_val))
        self.scroll_update(slider_val)

    # def color_region(self):


class RegionHighlightScroller(PlotScroller):
    def plot_init(self):
        pass

    def update_plots(self, plot_num):
        pass


class PlotScroller1D(PlotScroller):
    # initialize plots, return plot handles
    def plot_init(self):
        plts = []

        # normalize to first plot
        # dmin, dmax = np.min(self.data_sets[0]), np.max(self.data_sets[0])

        # for ind,ds_type in enumerate(self.data_sets[1:]):
        #     tmin,tmax = np.min(ds_type), np.max(ds_type)
        #     self.data_sets[ind+1] = (ds_type)*((dmax-dmin)/(tmax-tmin)) + dmin

        for ds_type, fmt, name in zip(self.data_sets, self.fmts, self.names):
            # print 'ds_type',ds_type
            if ds_type[0] != None:
                plts.append(
                    self.data_ax.plot(ds_type[0][0], ds_type[0][1], fmt, label=name)[0]
                )
            else:
                plts.append(None)

        # print [ds[0] for ds in ds_type]

        all_x = np.concatenate(
            [
                np.concatenate([ds[0] for ds in ds_type if ds is not None])
                for ds_type in self.data_sets
            ]
        )
        minx, maxx = np.min(all_x), np.max(all_x)

        all_y = np.concatenate(
            [
                np.concatenate([ds[1] for ds in ds_type if ds is not None])
                for ds_type in self.data_sets
            ]
        )
        miny, maxy = np.min(all_y), np.max(all_y)

        self.data_ax.set_xlim(minx, maxx)
        self.data_ax.set_ylim(miny, maxy)

        if not np.all([s is None for s in self.names]):
            self.data_ax.legend()
        self.data_plots = plts

    # initialize plots, return plot handles
    def update_plots(self, plot_num):
        for ind, ds in enumerate(self.data_sets):
            ds_plot = self.data_plots[ind]

            if ds[plot_num] is not None:
                x, y = ds[plot_num][0], ds[plot_num][1]

                # if ds_plot is None:

                try:
                    ds_plot.set_data(x, y)
                except AttributeError:
                    self.data_plots[ind] = self.data_ax.plot(
                        *self.data_sets[ind][plot_num]
                    )[0]
                self.data_plots[ind].set_visible(True)
            else:
                if self.data_plots[ind] is not None:
                    self.data_plots[ind].set_visible(False)

    @classmethod
    def add_range(cls, plot_data):
        return [(range(0, len(plot_data[0])), s) for s in plot_data]

    @classmethod
    def from_y_only_data(cls, data_sets, *args):
        return cls([cls.add_range(s) for s in data_sets], *args)

    def draw_hline(self, hline_value, *plot_args, **plot_kwargs):
        x_lim = self.data_ax.get_xlim()
        self.data_ax.plot(x_lim, [hline_value, hline_value], *plot_args, **plot_kwargs)
        self.data_ax.set_xlim(*x_lim)

    def draw_vline(self, vline_value, *plot_args, **plot_kwargs):
        y_lim = self.data_ax.get_ylim()
        self.data_ax.plot([vline_value, vline_value], y_lim, *plot_args, **plot_kwargs)
        self.data_ax.set_ylim(*y_lim)


class HighlightScroller1D(PlotScroller1D):
    def __init__(self, data_sets, region_edges, region_colors, region_data):
        if 0 not in region_edges:
            region_edges = np.concatenate(([0], region_edges))

        if len(data_sets[0][0][0]) not in region_edges:
            region_edges = np.concatenate((region_edges, [len(data_sets[0][0][0])]))

        self.region_colors = region_colors
        self.region_data = region_data
        self.region_edges = region_edges

        self.region_handles = []

        super().__init__(data_sets)

    def update_plots(self, plot_num):
        super().update_plots(plot_num)

        for ind, pat in enumerate(self.region_handles):
            pat.set_color(self.region_colors[self.region_data[self.cur_set][ind]])

    def plot_init(self):
        super().plot_init()

        low_edge = self.region_edges[:-1]
        high_edge = self.region_edges[1:]

        yl, yh = self.data_ax.get_ylim()

        from matplotlib.patches import Rectangle

        for l, h in zip(low_edge, high_edge):
            patch = Rectangle((l, yl), h - l, yh - yl, edgecolor="none", alpha=0.3)
            self.region_handles.append(patch)
            self.data_ax.add_patch(patch)


#
# plt.show()


class ImageScroller:
    DEFAULT_IMSHOW_KWARGS = dict(cmap="Greys", origin="lower", interpolation="None")

    def __init__(
        self,
        image_list,
        figure=None,
        num_hist_bins=100,
        scroll_callback=None,
        do_mask=False,
        im_thresh=None,
        window_start=None,
        annotation_lines=None,
        title=None,
        imshow_kwarg_override_dict=None,
    ):
        # self.images = image_list

        if do_mask:
            self.images = self.mask_images(image_list)
        else:
            self.images = [np.ma.MaskedArray(s, mask=None) for s in image_list]

        self.imshow_kwargs = self.DEFAULT_IMSHOW_KWARGS
        if imshow_kwarg_override_dict is not None:
            for key in imshow_kwarg_override_dict.keys():
                self.imshow_kwargs[key] = imshow_kwarg_override_dict[key]

        if annotation_lines is not None:
            assert len(annotation_lines) == len(self.images)
            self.anno_lines = annotation_lines

        self.scroll_callback = scroll_callback

        self.num_images = len(image_list)
        self.cur_img = 0
        self.last_img = 0
        self._num_hist_bins = num_hist_bins

        from matplotlib import gridspec

        gs = gridspec.GridSpec(
            2, 2, width_ratios=[0.9, 0.1], height_ratios=[0.95, 0.05]
        )

        if figure is None:
            self.fig = plt.figure()
        else:
            self.fig = figure

        self.img_ax = self.fig.add_subplot(gs[0])

        if title is not None:
            if len(title) == 1:
                self.titles = [title] * self.num_images
            else:
                assert len(title) == self.num_images
                self.titles = title
        else:
            self.titles = None
            # self.fig.suptitle(title)

        self.img_plot = self.init_plot()

        self._scroll_event_count = 0
        self.fig.canvas.mpl_connect("scroll_event", self.mouse_scroll)

        # setup slider
        self.slide_ax = self.fig.add_subplot(gs[2])
        self.slc_slider = Slider(
            self.slide_ax, "slice", 0, self.num_images - 1, valinit=0, valfmt="%d"
        )
        self.slc_slider.on_changed(self.slider_update)

        # setup histograms
        self.hist_ax = plt.subplot(gs[1])
        self.hist_ax.get_xaxis().set_ticks([])
        hists = [np.histogram(s[~s.mask], bins=num_hist_bins) for s in self.images]

        # self.hist_x = [np.log10(s[0]) for s in hists]
        # self.hist_x = [np.ma.masked_less(s, 0) for s in self.hist_x]
        self.hist_x = [s[0] for s in hists]
        self.hist_y = [s[1][0:-1] for s in hists]

        self.hist_plt = self.init_hist(self._num_hist_bins)

        self.hist_sel = SpanSelector(
            self.hist_ax,
            self.hist_select,
            "vertical",
            useblit=True,
            rectprops=dict(alpha=0.5, facecolor="red"),
            span_stays=True,
        )

        # self.hist_slider = VertSlider(self.hist_ax, '', 0.1, 10.0, valinit=0.1)

        if im_thresh is not None:
            assert len(im_thresh) == self.num_images
            self.im_thresh = im_thresh
        else:
            self.im_thresh = None
        self.patches = [None] * self.num_images

        self.update()
        hmin, hmax = self.get_hist_bounds()
        self.update_cmap(hmin, hmax * 1.1)

    def set_titles(self, titles):
        assert len(titles) == self.num_images
        self.titles = titles

        # plt.show()

    def set_img_extent(self, ext_y, ext_x):
        self.imshow_kwargs["extent"] = np.concatenate((ext_x, ext_y))
        del self.img_plot
        self.img_plot = self.init_plot()

    def add_patches(self, list_of_patches):
        assert len(list_of_patches) == self.num_images

        for ind, plt_patches, plist in zip(
            range(0, self.num_images), self.patches, list_of_patches
        ):
            try:
                some_object_iterator = iter(plist)
            except TypeError:
                plist = [plist]

            for ptch in plist:
                if self.patches[ind] is None:
                    self.patches[ind] = []
                if ptch not in self.patches[ind] and ptch is not None:
                    self.img_ax.add_patch(ptch)
                    ptch.set_visible(False)
                    self.patches[ind].append(ptch)

        for p in self.patches[self.cur_img]:
            p.set_visible(True)

    # def add_patches(self, list_of_patches):
    #
    #     assert len(list_of_patches) == self.num_images
    #
    #     for proj_patch,new_patch in zip(self.patches,list_of_patches):
    #         for ptch in new_patch:
    #             if ptch not in proj_patch:
    #                 proj_patch.append(ptch)
    #                 ptch.set_visible(False)
    #
    #                 if ptch not in self.img_ax.patches:
    #                     self.img_ax.add_patch(ptch)
    #
    #
    #     for p in list_of_patches[self.cur_img]:
    #         p.set_visible(True)

    def hist_select(self, min, max):
        self.update_cmap(min, max)

    def update_cmap(self, vmin, vmax):
        self.img_plot.set_clim(vmin=vmin, vmax=vmax)
        self.hist_ax.plot()
        # self.update()

    def mask_images(self, image_list, t_low=None, t_high=None):
        if t_high is None:
            t_high = np.percentile(image_list, 99)
        if t_low is None:
            t_low = np.percentile(image_list, 1)

        return [np.ma.masked_outside(s, t_low, t_high, copy=False) for s in image_list]

    def init_plot(self):
        # return self.img_ax.imshow(self.images[self.cur_img], cmap='Greys', origin='lower', interpolation='None')
        return self.img_ax.imshow(self.images[self.cur_img], **self.imshow_kwargs)

        # return self.img_ax.imshow(self.images[self.cur_img], cmap='Greys', origin='lower')

    def init_hist(self, num_bins):
        hist_plt = self.hist_ax.plot(
            self.hist_x[self.cur_img], self.hist_y[self.cur_img]
        )
        hmin, hmax = self.get_hist_bounds()
        self.hist_ax.set_ylim(hmin, hmax)
        self.hist_ax.set_xlim(
            np.min(self.hist_x[self.cur_img]), np.max(self.hist_x[self.cur_img]) * 1.1
        )
        return hist_plt[0]

    def get_hist_bounds(self):
        return np.min(self.hist_y), np.max(self.hist_y)
        # return np.min(self.hist_x[self.cur_img]), np.max(self.hist_x[self.cur_img])

    def update(self):
        self.display_img(self.cur_img)
        self.display_hist(self.cur_img)

        self.slc_slider.set_val(self.cur_img)

        if self.scroll_callback is not None:
            xlim, ylim = self.img_ax.get_xlim(), self.img_ax.get_ylim()
            self.scroll_callback(self)
            self.img_ax.set_xlim(xlim)
            self.img_ax.set_ylim(ylim)

        if self.im_thresh is not None:
            self.update_cmap(*self.im_thresh[self.cur_img])

        if self.titles is not None:
            self.fig.suptitle(self.titles[self.cur_img])

        if self.patches[self.cur_img] is not None:
            for p in self.patches[self.last_img]:
                p.set_visible(False)

            for p in self.patches[self.cur_img]:
                p.set_visible(True)

            pass

        self.fig.canvas.draw_idle()

    def display_img(self, image_num):
        assert 0 <= image_num < self.num_images
        self.img_plot.set_data(self.images[image_num])

    def display_hist(self, image_num):
        self.hist_plt.set_data(self.hist_x[self.cur_img], self.hist_y[self.cur_img])
        self.hist_ax.set_xlim(
            np.min(self.hist_x[self.cur_img]), np.max(self.hist_x[self.cur_img]) * 1.1
        )
        # self.hist_ax.hist(self.hists[self.cur_img], bins=self._num_hist_bins, orientation="horizontal")

    def scroll_update(self, img_num):
        if self.cur_img != img_num and self._scroll_event_count == 0:
            self._scroll_event_count += 1

            self.last_img = self.cur_img
            self.cur_img = int(img_num)

            if self.cur_img < 0:
                self.cur_img = 0
            elif self.cur_img >= self.num_images:
                self.cur_img = self.num_images - 1

            self.update()

            self._scroll_event_count -= 1

    def set_image_slice(self, img_num):
        self.scroll_update(img_num)

    def mouse_scroll(self, event):
        if event.inaxes is not None and event.inaxes == self.img_ax:
            self.scroll_update(self.cur_img + event.step)

    def slider_update(self, slider_val):
        slider_val = int(np.ceil(slider_val))
        self.scroll_update(slider_val)

    def make_movie(self, movie_file_path, dpi=150, frames=None):
        import numpy as np

        import matplotlib.pyplot as plt

        def update(i):
            self.last_img = self.cur_img
            self.cur_img = i
            self.update()

        self.hist_ax.set_visible(False)
        self.slide_ax.set_visible(False)

        # self.hist_ax.remove()
        # self.slide_ax.remove()

        self.img_ax.get_xaxis().set_ticks([])
        self.img_ax.get_yaxis().set_ticks([])
        plt.tight_layout()
        self.fig.canvas.draw()

        if frames is None:
            frames = np.arange(0, self.num_images)

        from matplotlib.animation import FuncAnimation

        anim = FuncAnimation(self.fig, update, frames=frames, interval=100)

        anim.save(movie_file_path, dpi=dpi, writer="imagemagick")

        # FFMpegWriter = manimation.writers['ffmpeg']
        # metadata = dict(title='Movie Test', artist='Matplotlib',
        #                 comment='Movie support!')
        # writer = FFMpegWriter(fps=20, metadata=metadata)
        #
        # with writer.saving(self.fig, movie_file_path, 200):
        #     for i in range(self.num_images):
        #         self.cur_img = i
        #         self.update()
        #         writer.grab_frame()

    def draw_vertical_line(self, x_coord, *plot_args, **plot_kwargs):
        ylim = self.img_ax.get_ylim()
        self.img_ax.plot([x_coord, x_coord], ylim, *plot_args, **plot_kwargs)
        self.img_ax.set_ylim(*ylim)

    def draw_horizontal_line(self, y_coord, *plot_args, **plot_kwargs):
        xlim = self.img_ax.get_xlim()
        self.img_ax.plot(xlim, [y_coord, y_coord], xlim, *plot_args, **plot_kwargs)
        self.img_ax.set_xlim(*xlim)


class ImageScrollerPercentWindow(ImageScroller):
    def __init__(self, imgs, w_low_percentile, w_high_percentile, **img_scroll_kwargs):
        super().__init__(imgs, **img_scroll_kwargs)

        self.clow = []
        self.chigh = []

        for yhist in self.hist_y:
            self.clow.append(np.percentile(yhist, w_low_percentile))
            self.chigh.append(np.percentile(yhist, w_high_percentile))

        self.set_cmap(self)
        self.scroll_callback = self.set_cmap

    def set_cmap(self, imgs):
        imgs.update_cmap(self.clow[self.cur_img], self.chigh[self.cur_img])


class ProfileImageScroller(ImageScroller):
    def __init__(self, img_list, plot_list, num_hist_bins=100, image_share=0.2):
        self.plot_list = plot_list

        self.plot_list = (
            plot_list * (np.shape(img_list[0])[1] * image_share) / np.max(plot_list)
        )

        self.cur_profile_plot = None

        super().__init__(img_list, num_hist_bins=100, scroll_callback=self.plot_profile)

    def plot_profile(self, img_scroller):
        try:
            self.cur_profile_plot.set_data(
                self.plot_list[img_scroller.cur_img], range(0, len(self.plot_list[0]))
            )
        except AttributeError:
            self.cur_profile_plot = img_scroller.img_ax.plot(
                self.plot_list[img_scroller.cur_img],
                range(0, len(self.plot_list[0])),
                "--r",
            )[0]


# class PixelThresholdImageScroller(ImageScroller):
#
#     def __init__(self, img_list, threshold_low=1, threshold_high=500):
#
#         self.thresh_low = threshold_low
#         self.thresh_high = threshold_high
#
#         self.pix_img = None
#         super(PixelThresholdImageScroller, self).__init__(img_list, scroll_callback=self.plot_pix)
#
#
#
#     def plot_pix(self, img_scroller):
#
#         self.pix_img[(self.images[self.cur_img] < self.thresh_high) & (self.images[self.cur_img] >= self.thresh_low)]
#
#         except AttributeError:
#             self.pix_img = np.ma.masked_where(,
#                 np.zeros(np.shape(self.images[0])))
#
#         # self.pix_img[np.where( (self.images[self.cur_img] >= self.thresh_high) | (self.images[self.cur_img] <= self.thresh_low))] = 1
#
#         try:
#             self.pixel_plot.set_data(self.pix_img)
#         except AttributeError:
#
#             self.pixel_plot = img_scroller.img_ax.imshow(self.pix_img)


class VertSlider(AxesWidget):
    """
    A slider representing a floating point range

    The following attributes are defined
      *ax*        : the slider :class:`matplotlib.axes.Axes` instance

      *val*       : the current slider value

      *vline*     : a :class:`matplotlib.lines.Line2D` instance
                     representing the initial value of the slider

      *poly*      : A :class:`matplotlib.patches.Polygon` instance
                     which is the slider knob

      *valfmt*    : the format string for formatting the slider text

      *label*     : a :class:`matplotlib.text.Text` instance
                     for the slider label

      *closedmin* : whether the slider is closed on the minimum

      *closedmax* : whether the slider is closed on the maximum

      *slidermin* : another slider - if not *None*, this slider must be
                     greater than *slidermin*

      *slidermax* : another slider - if not *None*, this slider must be
                     less than *slidermax*

      *dragging*  : allow for mouse dragging on slider

    Call :meth:`on_changed` to connect to the slider event
    """

    def __init__(
        self,
        ax,
        label,
        valmin,
        valmax,
        valinit=0.5,
        valfmt="%1.2f",
        closedmin=True,
        closedmax=True,
        slidermin=None,
        slidermax=None,
        dragging=True,
        **kwargs
    ):
        """
        Create a slider from *valmin* to *valmax* in axes *ax*

        *valinit*
            The slider initial position

        *label*
            The slider label

        *valfmt*
            Used to format the slider value

        *closedmin* and *closedmax*
            Indicate whether the slider interval is closed

        *slidermin* and *slidermax*
            Used to constrain the value of this slider to the values
            of other sliders.

        additional kwargs are passed on to ``self.poly`` which is the
        :class:`matplotlib.patches.Rectangle` which draws the slider
        knob.  See the :class:`matplotlib.patches.Rectangle` documentation
        valid property names (e.g., *facecolor*, *edgecolor*, *alpha*, ...)
        """
        AxesWidget.__init__(self, ax)

        self.valmin = valmin
        self.valmax = valmax
        self.val = valinit
        self.valinit = valinit
        self.poly = ax.axhspan(valmin, valinit, 0, 1, **kwargs)

        self.vline = ax.axhline(valinit, 0, 1, color="r", lw=1)

        self.valfmt = valfmt
        ax.set_xticks([])
        ax.set_ylim((valmin, valmax))
        ax.set_yticks([])
        ax.set_navigate(False)

        self.connect_event("button_press_event", self._update)
        self.connect_event("button_release_event", self._update)
        if dragging:
            self.connect_event("motion_notify_event", self._update)
        self.label = ax.text(
            0.5,
            1.03,
            label,
            transform=ax.transAxes,
            verticalalignment="center",
            horizontalalignment="center",
        )

        self.valtext = ax.text(
            0.5,
            -0.03,
            valfmt % valinit,
            transform=ax.transAxes,
            verticalalignment="center",
            horizontalalignment="center",
        )

        self.cnt = 0
        self.observers = {}

        self.closedmin = closedmin
        self.closedmax = closedmax
        self.slidermin = slidermin
        self.slidermax = slidermax
        self.drag_active = False

    def _update(self, event):
        """update the slider position"""
        if self.ignore(event):
            return

        if event.button != 1:
            return

        if event.name == "button_press_event" and event.inaxes == self.ax:
            self.drag_active = True
            event.canvas.grab_mouse(self.ax)

        if not self.drag_active:
            return

        elif (event.name == "button_release_event") or (
            event.name == "button_press_event" and event.inaxes != self.ax
        ):
            self.drag_active = False
            event.canvas.release_mouse(self.ax)
            return

        val = event.ydata
        if val <= self.valmin:
            if not self.closedmin:
                return
            val = self.valmin
        elif val >= self.valmax:
            if not self.closedmax:
                return
            val = self.valmax

        if self.slidermin is not None and val <= self.slidermin.val:
            if not self.closedmin:
                return
            val = self.slidermin.val

        if self.slidermax is not None and val >= self.slidermax.val:
            if not self.closedmax:
                return
            val = self.slidermax.val

        self.set_val(val)

    def set_val(self, val):
        xy = self.poly.xy
        xy[1] = 0, val
        xy[2] = 1, val
        self.poly.xy = xy
        self.valtext.set_text(self.valfmt % val)
        if self.drawon:
            self.ax.figure.canvas.draw()
        self.val = val
        if not self.eventson:
            return
        for cid, func in self.observers.iteritems():
            func(val)

    def on_changed(self, func):
        """
        When the slider value is changed, call *func* with the new
        slider position

        A connection id is returned which can be used to disconnect
        """
        cid = self.cnt
        self.observers[cid] = func
        self.cnt += 1
        return cid

    def disconnect(self, cid):
        """remove the observer with connection id *cid*"""
        try:
            del self.observers[cid]
        except KeyError:
            pass

    def reset(self):
        """reset the slider to the initial value if needed"""
        if self.val != self.valinit:
            self.set_val(self.valinit)
