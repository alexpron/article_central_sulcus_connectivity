from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

DEFAULT = mpl.cm.magma_r


def generate_colorbar(vmax=8000, step=500, path_fig=None, vmin=0, nb_levels=100, orientation='vertical', cmap=DEFAULT):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if vmin is not None and vmax is not None:
        m = plt.cm.ScalarMappable(cmap=cmap)
        m.set_clim(vmin, vmax)
        cbar = plt.colorbar(m, boundaries=np.linspace(vmin, vmax, nb_levels + 1), orientation=orientation)
        cbar.set_ticks(np.arange(vmin, vmax + step, step))
        ax.set_visible(False)
        if path_fig is not None:
            plt.savefig(path_fig, dpi=300, format='tif', )
            plt.close(fig)
        else:
            plt.show()
    pass


def subject_colorbar(path_fig, vmax=100, step=5):
    generate_colorbar(vmax=vmax, step=step, path_fig=path_fig)


def group_colorbar(path_fig):
    generate_colorbar(path_fig=path_fig)


if __name__ == '__main__':
    from configuration.configuration import GROUP_CBAR, SUBJ_CBAR

    group_colorbar(GROUP_CBAR)
    subject_colorbar(SUBJ_CBAR)
