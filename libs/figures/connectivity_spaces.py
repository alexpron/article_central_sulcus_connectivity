"""
Functions dedicated to plot connectivity space, connectivity profiles and
additionnal information such as PPFM position
"""

import numpy as np
from skimage.feature import (
    peak_local_max,
)  # not wonderful mixes computation and display
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import colors
import matplotlib.cm as cm

from libs.tools.ppfm import (
    get_hemisphere_group_pp,
    get_hemisphere_subject_pp,
    ppfm_coords_2_str,
)


# DEFAULTS adapted to Brain Structure and Function format
# ------------------------------------------------------------------------------
BSFONT = "Arial"
TEXTFONTSIZE = 15
# default resolution required for BSF figures
DPI = 300
# default format required for BSF figures
FORMAT = "tif"
# default number of level set for density display

# DEFAULTS for connectivity space figures
# ------------------------------------------------------------------------------
COLORS = ("red", "blue", "orange", "green", "purple", "black")
XLABEL = "Pre-Central Coordinate"
YLABEL = "Post-Central Coordinate"
clustering_colors = COLORS[:-1]


def discrete_colormap(list_colors, boundaries):
    """
    Generate a discrete Matplotlib colormap from a set of colors
    :param list_colors:
    :param boundaries:
    :return:
    """
    cmap = colors.ListedColormap(list_colors)
    norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)
    return cmap, norm


def hierarchical_clustering_colormap(colors=COLORS):
    """
    Generate colormap for connectivity space clusters obtained through hierarchical clustering
    """
    boundaries = np.arange(len(colors) + 1)
    cmap, norm = discrete_colormap(colors, boundaries)
    return cmap, norm


def dbscan_clustering_colormap(colors=COLORS):
    """
    Generate colormap for connectivity space clusters obtained through dbscan clustering
    :param colors:
    :return:
    """
    boundaries = np.arange(-1, len(colors))
    cmap, norm = discrete_colormap(colors, boundaries)
    return cmap, norm


clustering_color_map = {
    "default": hierarchical_clustering_colormap(),
    "dbscan": dbscan_clustering_colormap(),
}


def connectivity_space(
    path_fig=None,
    title=None,
    background_color=None,
    font=BSFONT,
    fontsize=TEXTFONTSIZE,
    format=FORMAT,
    dpi=DPI,
    xlabel=XLABEL,
    ylabel=YLABEL,

):
    """
    Canvas to plot connectivity profile that respects Brain Structure and Function
    requirements
    :param path_fig:
    :param title:
    :param xlabel:
    :param ylabel:
    :return:
    """
    # general figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if background_color is not None:
        ax.set_facecolor('grey')
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass
    # Label and dimensions of the axes
    plt.xlabel(xlabel, fontsize=fontsize, fontname=font)
    plt.ylabel(ylabel, fontsize=fontsize, fontname=font)
    plt.xticks(np.arange(0, 110, 10), np.arange(0, 110, 10))
    plt.yticks(np.arange(0, 110, 10), np.arange(0, 110, 10))
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.text(-15, -7, "Ventral", fontsize=fontsize, weight="bold", fontname=font)
    plt.text(92, -7, "Dorsal", fontsize=fontsize, weight="bold", fontname=font)
    plt.text(-15, 98, "Dorsal", fontsize=fontsize, weight="bold", fontname=font)

    # Draw the diagonal of the space
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color="grey")
    # add grid to easily spot positions
    ##plt.grid()
    if path_fig is not None:
        plt.savefig(path_fig, format=format, dpi=dpi, bbox_inches="tight")
        plt.close(fig)
    return fig, ax


def crests_as_arrows_display(
    figure, path_fig=None, font=BSFONT, fontsize=TEXTFONTSIZE, format=FORMAT, dpi=DPI
):
    """
    :param path_fig:
    :param title:
    :param font:
    :param fontsize:
    :param format:
    :param dpi:
    :param xlabel:
    :param ylabel:
    :return:
    """

    ax = figure.get_axes()[0]
    # Pre-Central Gyrus Crest
    ax.arrow(x=0, y=0, dx=100, dy=0, color="xkcd:orange", linewidth=10)
    # Post-Central Gyrus Crest
    ax.arrow(x=0, y=0, dx=0, dy=100, color="purple", linewidth=10)

    ax.plot(
        [30, 30], [0, 60], color="xkcd:orange", linestyle="--", linewidth=2, alpha=1
    )
    ax.plot([0, 30], [60, 60], color="purple", linestyle="--", linewidth=2, alpha=1)
    ax.plot(
        [45, 30], [45, 60], color="dodgerblue", linestyle="--", linewidth=2, alpha=1
    )

    ax.arrow(x=0, y=0, dx=100, dy=100, color="dodgerblue", linewidth=5)
    ax.arrow(x=0, y=0, dx=-50, dy=50, color="fuchsia", linewidth=10)

    ax.scatter([30], [60], marker="+", color="black", s=150)
    ax.annotate(
        "",
        xy=(-0.5, 0.5),
        xycoords="axes fraction",
        xytext=(0, 0),
        arrowprops=dict(arrowstyle="simple", color="fuchsia", linewidth=4),
    )
    plt.text(
        35,
        30,
        "Diagonal Coordinate (Diag_C)",
        fontsize=15,
        fontname=font,
        rotation=45,
        color="dodgerblue",
    )

    if path_fig is not None:
        plt.savefig(path_fig, format=format, dpi=dpi, bbox_inches="tight")
        plt.close(figure)

    return figure


def density_display(
    X,
    Y,
    density,
    figure,
    cmap=cm.magma_r,
    nb_levels=150,
    vmin=None,
    vmax=None,
    colorbar=True,
    colorbar_ticks_step=500,
):
    """
    Default U-fibres density display
    :param X:
    :param Y:
    :param density:
    :param figure:
    :param cmap:
    :param nb_levels:
    :param vmin:
    :param vmax:
    :return:
    """
    ax = figure.get_axes()[0]
    if vmin is not None and vmax is not None:
        ax.contourf(X, Y, density, nb_levels, cmap=cmap, vmin=vmin, vmax=vmax)
        if colorbar:
            m = plt.cm.ScalarMappable(cmap=cmap)
            m.set_array(density)
            m.set_clim(vmin, vmax)
            colorbar = plt.colorbar(
                m, boundaries=np.linspace(vmin, vmax, nb_levels + 1)
            )
            colorbar.set_ticks(
                np.arange(vmin, vmax + colorbar_ticks_step, colorbar_ticks_step)
            )
            colorbar.set_ticklabels(
                np.arange(vmin, vmax + colorbar_ticks_step, colorbar_ticks_step)
            )
    else:
        dens = ax.contourf(X, Y, density, nb_levels, cmap=cmap)
        if colorbar:
            figure.colorbar(dens, ax=ax)
    pass


def scatter_display(
    points, labels, figure, cmap="default", path_fig=None, title=None, alpha=1
):
    """
    :param points: the b_coordinates of the streamlines in the 2D space (a Nx2 ndarray)
    :param labels: labels assigned to each point after clustering. a (N,) nddarray
    :param pli_passage: the b_coordinates of the knob a (2,) ndarray
    :param path_fig: the path to save the figure, the type of the figure will be determined from the path
    :param title: the title of the figure
    :return: None
    """
    # figure setting
    ax = figure.get_axes()[0]
    # display the points as dots
    if labels is not None:
        cmap, norm = clustering_color_map[cmap]
        label_values = np.unique(labels)
        for i, l in enumerate(label_values):
            p = points[labels == l]
            new_l = labels[labels == l]
            ax.scatter(p[:, 0], p[:, 1], c=new_l, cmap=cmap, norm=norm, alpha=alpha)
    else:
        ax.scatter(points[:, 0], points[:, 1])

    if path_fig is not None:
        plt.savefig(
            path_fig, dpi=300, format="tif", bbox_inches="tight", pad_inches=0.0
        )
        plt.close(figure)
    else:
        pass


def ppfm_display(
    figure, ppfm, label, color="b", linewidth=2, marker="x", markersize=300
):
    """
    :param figure:
    :param ppfm:
    :param label:
    :param color:
    :param linewidth:
    :param marker:
    :param markersize:
    :return:
    """
    ax = figure.get_axes()[0]
    ax.plot(
        [0, ppfm[0]],
        [ppfm[1], ppfm[1]],
        color,
        linestyle="dashed",
        linewidth=linewidth - 1,
        alpha=1,
    )
    ax.plot(
        [ppfm[0], ppfm[0]],
        [0, ppfm[1]],
        color,
        linestyle="dashed",
        linewidth=linewidth - 1,
        alpha=1,
    )
    coords = ppfm_coords_2_str(ppfm)
    final_label = label + " " + coords
    ax.scatter(
        [ppfm[0]],
        [ppfm[1]],
        marker=marker,
        color=color,
        s=markersize,
        label=final_label,
    )
    pass


def density_maxima_display(figure, density):
    """

    :param figure:
    :param density:
    :return:
    """
    peaks_indexes = peak_local_max(
        density,
        3,
        threshold_rel=0.30,
        threshold_abs=threshold_abs,
        exclude_border=False,
    )
    pass


def connectivity_profile(
    X,
    Y,
    density,
    path_fig=None,
    title=None,
    nb_levels=150,
    vmin=None,
    vmax=None,
    colorbar=True,
    colorbar_tiks_step=500,
    ppfm=None,
    ppfm_label=None,
):

    # figure setting
    figure, ax = connectivity_space(title=title)
    # density display
    density_display(
        X,
        Y,
        density,
        figure,
        nb_levels=nb_levels,
        vmin=vmin,
        vmax=vmax,
        colorbar=colorbar,
    )
    # add ppfm position as blue cross
    if ppfm is not None:
        ppfm_display(figure, ppfm, ppfm_label)
    plt.grid()
    plt.legend()
    if path_fig is not None:
        plt.savefig(
            path_fig, dpi=DPI, format=FORMAT, bbox_inches="tight", pad_inches=0.0
        )
        plt.close(figure)
    else:
        return figure
    pass


def connectivity_profile_with_maxima(
    X,
    Y,
    density,
    path_fig=None,
    title=None,
    nb_levels=150,
    vmin=None,
    vmax=None,
    colorbar=True,
    ppfm=None,
    ppfm_label=None,
    threshold_abs=50,
):
    """

    :param X:
    :param Y:
    :param density:
    :param path_fig:
    :param title:
    :param nb_levels:
    :param vmin:
    :param vmax:
    :param colorbar:
    :param ppfm:
    :param ppfm_label:
    :param threshold_abs:
    :return:
    """

    # figure setting
    figure, ax = connectivity_space(title=title)
    # density display
    density_display(
        X,
        Y,
        density,
        figure,
        nb_levels=nb_levels,
        vmin=vmin,
        vmax=vmax,
        colorbar=colorbar,
    )
    # add ppfm position as blue cross
    if ppfm is not None:
        ppfm_display(figure, ppfm, ppfm_label)

    plt.grid()
    plt.legend()
    if path_fig is not None:
        plt.savefig(
            path_fig, dpi=DPI, format=FORMAT, bbox_inches="tight", pad_inches=0.0
        )
        plt.close(figure)
    else:
        return figure


def draw_ellipse(ax, mu, sigma, color="k", linewidth=4, marker="+", markersize=150):
    """
    Based on
    http://stackoverflow.com/questions/17952171/not-sure-how-to-fit-data-with-a-gaussian-python.
    """

    # Compute eigenvalues and associated eigenvectors
    vals, vecs = np.linalg.eigh(sigma)

    # Compute "tilt" of ellipse using first eigenvector
    x, y = vecs[:, 0]
    theta = np.degrees(np.arctan2(y, x))

    # Eigenvalues give length of ellipse along each eigenvector
    w, h = 2 * np.sqrt(vals)

    # ax.tick_params(axis='both', which='major', labelsize=20)
    ellipse = Ellipse(
        mu, w, h, theta, fill=False, edgecolor=color, linewidth=linewidth
    )  # color="k")
    # ellipse.set_clip_box(ax.bbox)
    ellipse.set_alpha(1)
    ax.add_patch(ellipse)
    ax.scatter(
        mu[0], mu[1], marker=marker, s=markersize, color=color, linewidth=linewidth
    )
    return ax


def clusters_as_ellipses_display(
    figure, means, covariances, colors=clustering_colors, path_fig=None, title=None,
):
    """
    :param figure:
    :param means:
    :param covariances:
    :param colors:
    :param path_fig:
    :param title:
    :return:
    """
    ax = figure.get_axes()[0]
    for i, m in enumerate(means):
        draw_ellipse(ax, m, covariances[i], color=colors[i])

    # plt.legend()
    if path_fig is not None:
        plt.savefig(
            path_fig, dpi=300, format="tif", bbox_inches="tight", pad_inches=0.0
        )
        plt.close(fig)
    else:
        plt.show()
    pass


def clusters_as_dots(
    dots, labels, path_fig=None, ppfm=None, ppfm_label=None, title=None
):
    # figure setting
    figure, ax = connectivity_space(title=title)
    ax.set_facecolor('grey')
    scatter_display(dots, labels, figure)
    if ppfm is not None:
        ppfm_display(figure, ppfm, ppfm_label)
    plt.grid()
    plt.legend()
    if path_fig is not None:
        plt.savefig(
            path_fig, dpi=DPI, format=FORMAT, bbox_inches="tight", pad_inches=0.0
        )
        plt.close(figure)
    else:
        pass
