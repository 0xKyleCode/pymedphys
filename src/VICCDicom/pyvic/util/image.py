import abc
import numpy as np
from matplotlib.patches import Ellipse
from skimage.filters import threshold_otsu


from pyvic.util.data_structures import NDVoxelArray, DataSet1D
from pyvic.util.numeric import (
    rotatedRectWithMaxArea,
    get_consecutive_groups,
    fit_3d_gauss,
    fit_2d_gauss,
)
from pyvic.util.plotting import plot_horizontal_line, plot_vertical_line
from pyvic.util.utils import multi_process_func
from pyvic.util.ndarray import coordmax, central_subset
from pyvic.util.gui import NDVoxelPlotter


def sector_mask(shape, centre, radius, angle_range):
    """
    Return a boolean mask for a circular sector. The start/stop angles in
    `angle_range` should be given in clockwise order.
    """

    x, y = np.ogrid[: shape[0], : shape[1]]
    cx, cy = centre
    tmin, tmax = np.deg2rad(angle_range)

    # ensure stop angle > start angle
    if tmax < tmin:
        tmax += 2 * np.pi

    # convert cartesian --> polar coordinates
    r2 = (x - cx) * (x - cx) + (y - cy) * (y - cy)
    theta = np.arctan2(x - cx, y - cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= 2 * np.pi

    # circular mask
    circmask = r2 <= radius * radius

    # angular mask
    anglemask = theta <= (tmax - tmin)

    return circmask * anglemask


def sphere_sector_mask(shape, centre, radius, angle_range, phirange):
    """
    Return a boolean mask for a circular sector. The start/stop angles in
    `angle_range` should be given in clockwise order.
    """

    x, y, z = np.ogrid[: shape[0], : shape[1], : shape[2]]
    cx, cy, cz = centre
    tmin, tmax = np.deg2rad(angle_range)
    pmin, pmax = np.deg2rad(phirange)

    # ensure stop angle > start angle
    if tmax < tmin:
        tmax += 2 * np.pi

    pmin %= np.pi
    pmax %= np.pi

    # convert cartesian --> polar coordinates
    r2 = (x - cx) * (x - cx) + (y - cy) * (y - cy) + (z - cz) * (z - cz)
    theta = np.arctan2(x - cx, y - cy) - tmin
    phi = np.arccos(np.ma.divide(z - cz, np.sqrt(r2)))

    # print np.min(phi), np.max(phi)
    # wrap angles between 0 and 2*pi
    theta %= 2 * np.pi
    phi %= np.pi

    # circular mask
    circmask = r2 <= radius * radius

    # angular mask
    anglemask = theta <= (tmax - tmin)

    if pmin == pmax == 0:
        pmax = np.pi
    phimask = (phi >= pmin) & (phi <= pmax)

    return circmask * anglemask  # *phimask


def ellipse_sector_mask(shape, centre, r, angle_range, phirange):
    """
    Return a boolean mask for a circular sector. The start/stop angles in
    `angle_range` should be given in clockwise order.
    """

    x, y, z = np.ogrid[: shape[0], : shape[1], : shape[2]]
    cx, cy, cz = centre
    tmin, tmax = np.deg2rad(angle_range)
    pmin, pmax = np.deg2rad(phirange)

    # ensure stop angle > start angle
    if tmax < tmin:
        tmax += 2 * np.pi

    pmin %= np.pi
    pmax %= np.pi

    # convert cartesian --> polar coordinates
    r2 = ((x - cx) / r[0]) ** 2 + ((y - cy) / (r[1])) ** 2 + ((z - cz) / r[2]) ** 2
    theta = np.arctan2(x - cx, y - cy) - tmin
    phi = np.arccos(np.ma.divide(z - cz, np.sqrt(r2)))

    # print np.min(phi), np.max(phi)
    # wrap angles between 0 and 2*pi
    theta %= 2 * np.pi
    phi %= np.pi

    # circular mask
    circmask = r2 <= 1

    # angular mask
    anglemask = theta <= (tmax - tmin)

    if pmin == pmax == 0:
        pmax = np.pi
    phimask = (phi >= pmin) & (phi <= pmax)

    return circmask * anglemask  # *phimask


def circular_mask(shape, centre, radius):
    return sector_mask(shape, centre, radius, [0, 360])


def sphere_mask(shape, centre, radius, xy_extension_deg=[0, 360], phirange=[0, 180]):
    return sphere_sector_mask(shape, centre, radius, xy_extension_deg, phirange)


def ellipse_mask(shape, centre, radius, xy_extension_deg=[0, 360], phirange=[0, 180]):
    return ellipse_sector_mask(shape, centre, radius, xy_extension_deg, phirange)


@multi_process_func([0])
def mark_edges(slice):
    """
    given an arrea of 0, 1, find row groupings of 1's and mark the edges
    :param slice: arraey of 0, 1 (masking)
    :return: array marking boundaries of 0's and 1s
    """
    edges = np.zeros_like(slice)

    for row, erow in zip(slice, edges):
        reg = np.where(row == 1)[0]

        for grp in get_consecutive_groups(reg):
            erow[grp[0]] = 1
            erow[grp[-1]] = 1

    return edges


def otsu_threshold(pa, show_plot=False):
    thresh = threshold_otsu(pa)
    # print(thresh)
    image = pa
    thresh = threshold_otsu(pa)
    binary = pa < thresh
    if show_plot:
        from matplotlib import pyplot as plt

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


def find_vertical_edge(array_2d, num_pix_mean_buff=20, show_plot=False):
    """
    Find vertical edge in image (uses y summation of profile, mean values of buffer pixels)
    :param array_2d: 2d array containing image
    :param num_pix_mean_buff: number of pixels to use on sides for mean value calculation
    :param show_plot: show results
    :return: (float) x location of edge
    """
    import numpy as np

    ymesh = array_2d.coordinate_mesh[0]
    xmesh = array_2d.coordinate_mesh[1]
    profile = np.sum(array_2d, axis=0)

    ds = DataSet1D(xmesh, profile)
    m1 = np.mean(profile[0:num_pix_mean_buff])
    m2 = np.mean(profile[-1 * num_pix_mean_buff :])
    mval = np.mean([m1, m2])
    edge_x = ds.findY(mval)

    if show_plot:
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots()
        # ax.plot(profile)
        ds.plot(ax)
        ax.plot([edge_x], [mval], "+r")
        # ax.imshow(left_edge)
        # tbepi.plot(ax)
        # plot_vertical_line(ax, rough_xmin, fmt='--g')
        # plot_vertical_line(ax, rough_xmax, fmt='--g')
        # plot_horizontal_line(ax, rough_ymin,fmt='--g' )
        # plot_horizontal_line(ax, rough_ymax,fmt='--g' )
        plt.show()
    return edge_x


def find_horizontal_edge(array_2d, num_pix_mean_buff=20, show_plot=False):
    """
    Find horizontal edge in image (uses y summation of profile, mean values of buffer pixels)
    :param array_2d: (NDvoxelarray) 2d array containing image
    :param num_pix_mean_buff: number of pixels to use on sides for mean value calculation
    :param show_plot: show results
    :return: (float) x location of edge
    """
    import numpy as np

    assert isinstance(array_2d, NDVoxelArray)

    ymesh = array_2d.coordinate_mesh[0]
    xmesh = array_2d.coordinate_mesh[1]
    profile = np.sum(array_2d, axis=1)

    ds = DataSet1D(ymesh, profile)
    m1 = np.mean(profile[0:num_pix_mean_buff])
    m2 = np.mean(profile[-1 * num_pix_mean_buff :])
    mval = np.mean([m1, m2])

    edge_x = ds.findY(mval)

    if show_plot:
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots()
        ds.plot(ax)
        ax.plot([edge_x], [mval], "+r")
        plt.show()
    return edge_x


from abc import ABCMeta, abstractproperty


class BBFinder:
    __metaclass__ = ABCMeta

    @property
    @abc.abstractmethod
    def BB_ROI_DICT(self):
        pass

    @property
    @abc.abstractmethod
    def BB_SIZE_GUESS(self):
        pass

    @property
    @abc.abstractmethod
    def BB_FIT_WINDOW(self):
        pass

    @property
    @abc.abstractmethod
    def FIT_HU_THRESHOLD(self):
        pass

    def __init__(
        self, img: NDVoxelArray, show_plot: bool = False, save_plot_dir: str = None
    ) -> "BBFinder":
        """

        :type img: CTScan
        """
        self.bb_locations = {}
        self.img = img

        for name, loc in self.BB_ROI_DICT.items():
            # select bb ROI
            # print(loc)
            bb_roi = img.subset_by_percent(loc)

            # find maximum coordinate

            bb_coords_guess = coordmax(bb_roi)

            # shrink ROI around bb to 10mm

            bb_roi = central_subset(
                bb_roi, bb_coords_guess, self.BB_FIT_WINDOW, do_clipping=True
            )

            # 3D gaussian fit BB
            if img.nDim == 3:
                bb_coords, bb_sig = fit_3d_gauss(
                    bb_roi,
                    bb_coords_guess,
                    [self.BB_SIZE_GUESS, self.BB_SIZE_GUESS, self.BB_SIZE_GUESS],
                    lower_threshold=self.FIT_HU_THRESHOLD,
                )

                if show_plot or save_plot_dir is not None:
                    bb_index = bb_roi.coord_tuple_to_nearest_index(bb_coords)
                    from matplotlib import pyplot as plt

                    fig, ax = plt.subplots(1, 3)

                    ndv_plotter = NDVoxelPlotter(bb_roi)
                    ndv_plotter.plot_z_slice(ax[0], bb_index[0])
                    ndv_plotter.plot_point_zplane(
                        ax[0], bb_coords, "+g", markersize=10, mew=5
                    )

                    ndv_plotter.plot_y_slice(ax[1], bb_index[1])
                    ndv_plotter.plot_point_yplane(
                        ax[1], bb_coords, "+g", markersize=10, mew=5
                    )

                    ndv_plotter.plot_x_slice(ax[2], bb_index[2])
                    ndv_plotter.plot_point_xplane(
                        ax[2], bb_coords, "+g", markersize=10, mew=5
                    )

                    if save_plot_dir:
                        fig.savefig(
                            save_plot_dir
                            + "/%s_%sbb_plot.png"
                            % (img.aquisition_date.__str__().replace(" ", "_"), name)
                        )

                    if show_plot:
                        plt.show()

            elif img.nDim == 2:
                bb_coords, bb_sig = fit_2d_gauss(
                    bb_roi,
                    bb_coords_guess,
                    [self.BB_SIZE_GUESS, self.BB_SIZE_GUESS],
                    show_plot=False,
                    lower_threshold=self.FIT_HU_THRESHOLD,
                )
            else:
                raise NotImplementedError(
                    "BBFinder only implemented for 2,3 dim, not %s" % img.nDim
                )

            # get closest slice index for bb x,y,z centre
            #

            self.bb_locations[name] = bb_coords

        if show_plot:
            if img.nDim == 2:
                from matplotlib import pyplot as plt

                fig, ax = plt.subplots()
                ax.imshow(img, **img.PLOT_KWARGS)
                for name, bb in self.bb_locations.items():
                    # print(bb)
                    ax.add_artist(
                        Ellipse(
                            xy=(bb[1], bb[0]),
                            width=self.BB_SIZE_GUESS,
                            height=self.BB_SIZE_GUESS,
                            fill=False,
                            ec="r",
                        )
                    )

                plt.show()

            else:
                pass

    def __str__(self):
        to_string = ""
        to_string += "{} ({})\n".format(self.img.series_id, self.img.aquisition_date)

        for name, locs in self.bb_locations.iteritems():
            to_string += "{} \t-\t (x:{:0.2f}  y:{:0.2f}  z:{:0.2f})\n".format(
                name,
                locs[2],
                locs[1],
                locs[0],
            )
        return to_string

    def draw_bb(self, ax, name):
        bb = self.bb_locations[name]
        ax.add_artist(
            Ellipse(
                xy=(bb[1], bb[0]),
                width=self.BB_SIZE_GUESS,
                height=self.BB_SIZE_GUESS,
                fill=False,
                ec="r",
            )
        )

    def draw_all_bbs(self, ax):
        for name in self.bb_locations.keys():
            self.draw_bb(ax, name)


class LAPBBFinder(BBFinder):
    BB_FIT_WINDOW = 10
    BB_SIZE_GUESS = 1
    FIT_HU_THRESHOLD = 3000
    BB_ROI_DICT = {
        "left": [(0, 1), (0, 1), (0, 1 / 3.0)],
        "top": [(0, 1), (0.5, 1), (1 / 3.0, 2 / 3.0)],
        "bottom": [(0, 1), (0, 0.5), (1 / 3.0, 2 / 3.0)],
        "right": [(0, 1), (0, 1), (2 / 3.0, 1)],
    }


class RadLightCoincidentBBFinder(BBFinder):
    BB_FIT_WINDOW = 10
    BB_SIZE_GUESS = 2
    FIT_HU_THRESHOLD = "otsu"
    BB_ROI_DICT = {
        0: [(0.2, 0.4), (0.25, 0.4)],
        1: [(0.2, 0.4), (0.4, 0.6)],
        2: [(0.2, 0.4), (0.6, 0.75)],
        3: [(0.4, 0.6), (0.25, 0.4)],
        4: [(0.4, 0.6), (0.4, 0.6)],
        5: [(0.4, 0.6), (0.6, 0.75)],
        6: [(0.6, 0.8), (0.25, 0.4)],
        7: [(0.6, 0.8), (0.4, 0.6)],
        8: [(0.6, 0.8), (0.6, 0.75)],
    }


def find_square_field(image_2d_ndvoxel, threshold=None, show_plot=False):
    """
    Find square field in image, note that threshold works
    :param image_2d_ndvoxel: (NDVoxelArray) 2d dimage
    :param threshold: threshold value, default otsu
    :return: (bottom,top),(left,right)
    """

    if threshold is None:
        threshold = otsu_threshold(image_2d_ndvoxel)

    import numpy as np

    roi = np.where(image_2d_ndvoxel < threshold)
    # rough ROI edges
    rough_xmin = int(np.min(roi[1]))
    rough_xmax = int(np.max(roi[1]))
    rough_ymin = int(np.min(roi[0]))
    rough_ymax = int(np.max(roi[0]))
    roi_edge_buffer_mm = 20
    nbuf = int(np.ceil(roi_edge_buffer_mm / image_2d_ndvoxel.voxdims[1]))

    left_image = image_2d_ndvoxel.subset_by_index(
        [(rough_ymin + nbuf, rough_ymax - nbuf), (rough_xmin - nbuf, rough_xmin + nbuf)]
    )  # type: NDVoxelArray
    left_edge = find_vertical_edge(left_image, nbuf, show_plot=show_plot)
    right_image = image_2d_ndvoxel.subset_by_index(
        [(rough_ymin + nbuf, rough_ymax - nbuf), (rough_xmax - nbuf, rough_xmax + nbuf)]
    )  # type: NDVoxelArray
    right_edge = find_vertical_edge(right_image, nbuf, show_plot=show_plot)
    top_image = image_2d_ndvoxel.subset_by_index(
        [(rough_ymax - nbuf, rough_ymax + nbuf), (rough_xmin + nbuf, rough_xmax - nbuf)]
    )  # type: NDVoxelArray
    top_edge = find_horizontal_edge(top_image, nbuf, show_plot=show_plot)
    bottom_image = image_2d_ndvoxel.subset_by_index(
        [(rough_ymin - nbuf, rough_ymin + nbuf), (rough_xmin + nbuf, rough_xmax - nbuf)]
    )  # type: NDVoxelArray
    bottom_edge = find_horizontal_edge(bottom_image, nbuf, show_plot=show_plot)

    if show_plot:
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots()
        ax.imshow(
            image_2d_ndvoxel,
            origin="lower",
            extent=image_2d_ndvoxel.extent,
            interpolation="None",
            cmap="Greys_r",
        )

        plot_horizontal_line(ax, top_edge, "--g")
        plot_horizontal_line(ax, bottom_edge, "--g")

        plot_vertical_line(ax, left_edge, "--g")
        plot_vertical_line(ax, right_edge, "--g")
        plt.show()

    return (bottom_edge, top_edge), (left_edge, right_edge)


def rotate_with_crop(image: NDVoxelArray, rot: float, show_plot: bool = False):
    from scipy.ndimage import rotate

    if not np.all([s == 0 for s in image.origin]):
        raise NotImplementedError()
    if not image.nDim == 2:
        raise NotImplementedError()

    new_img_reg = rotate(image, angle=rot, reshape=False, mode="constant", cval=np.nan)

    new_img_reg = NDVoxelArray(new_img_reg, voxdims=image.voxdims)  # type: NDVoxelArray

    h, w = new_img_reg.shape
    wr, hr = rotatedRectWithMaxArea(w, h, rot)
    wr, hr = np.floor(wr), np.floor(hr)

    my, mx = h / 2.0, w / 2.0
    ylow, yhigh = np.ceil(my - (hr / 2.0)), np.floor(my + (hr / 2.0))
    xlow, xhigh = np.ceil(mx - (wr / 2.0)), np.floor(mx + (wr / 2.0))

    if show_plot:
        from matplotlib import pyplot as plt

        fig, ax = plt.subplots(1, 2)
        ax[0].imshow(new_img_reg, origin="lower")
        ax[1].imshow(
            new_img_reg.subset_by_index([(ylow, yhigh), (xlow, xhigh)]), origin="lower"
        )
        plt.show()

    return new_img_reg.subset_by_index([(ylow, yhigh), (xlow, xhigh)])
