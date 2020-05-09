import numpy as np
from skimage.feature import peak_local_max
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib import colors
import matplotlib.cm as cm

COLORS = ['red', 'blue', 'orange', 'green', 'purple', 'black']

def discrete_colormap(list_colors, boundaries):
    cmap = colors.ListedColormap(list_colors)
    norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)
    return cmap, norm

def hierarchical_clustering_colormap(colors=COLORS):
    boundaries = np.arange(len(colors) + 1)
    cmap,norm = discrete_colormap(colors,boundaries)
    return cmap, norm

def dbscan_clustering_colormap(colors=COLORS):
    boundaries = np.arange(-1,len(colors))
    cmap, norm = discrete_colormap(colors, boundaries)
    return cmap, norm

clustering_color_map = {'default':hierarchical_clustering_colormap(), 'dbscan':dbscan_clustering_colormap()}


XLABEL = 'Pre-Central Coordinate'
YLABEL = 'Post-Central Coordinate'


def default_plot(path_fig=None, title=None, xlabel=XLABEL, ylabel=YLABEL):
    """
    Canvas to plot connectivity profile that respect Brain Structure and Function
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
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass
    # Label and dimensions of the axes
    plt.xlabel(xlabel, fontsize=15, fontname='Arial')
    plt.ylabel(ylabel, fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.text(-20, -7, 'Ventral', fontsize=15, weight='bold',fontname='Arial')
    plt.text(100, -7, 'Dorsal', fontsize=15, weight='bold',fontname='Arial')
    plt.text(-20, 100, 'Dorsal', fontsize=15, weight='bold',fontname='Arial')
    # Draw the diagonal of the space
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')
    #add grid to easily spot positions
    plt.grid()
    if path_fig is not None:
        plt.savefig(path_fig)
        plt.close(fig)
    return fig, ax




def scatter_plot(points,labels=None, pli_passage=None, path_fig=None, title=None,colormap=None, alpha=1):
    '''
    :param points: the b_coordinates of the streamlines in the 2D space (a Nx2 ndarray)
    :param labels: labels assigned to each point after clustering. a (N,) nddarray
    :param pli_passage: the b_coordinates of the knob a (2,) ndarray
    :param path_fig: the path to save the figure, the type of the figure will be determined from the path
    :param title: the title of the figure
    :return: None
    '''
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10,10)
    ax.set_facecolor('grey')
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass
        #plt.title('Connectivity Space')
    #Label and dimensions of the axes
    plt.xlabel('Pre-Central Coordinate', fontsize=15)
    plt.ylabel('Post-Central Coordinate', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0, 100, 11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(90, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold')
    #trace de la diagonale comme reference de coordonnees
    x = np.linspace(0,100,1000)
    plt.plot(x,x,color='grey')
    if pli_passage is not None:
    #trace de la position  du pli_passage
        plt.plot([0, pli_passage[0]], [pli_passage[1], pli_passage[1]], 'b-', linewidth=2, alpha=1)
        plt.plot([pli_passage[0], pli_passage[0]], [0, pli_passage[1]], 'b-', linewidth=2, alpha=1)
        plt.scatter([pli_passage[0]], [pli_passage[1]], marker='+', color='blue', s=150, label="Individual PPFM  (" + str(np.round(pli_passage[0][0],decimals=2)) + ' ; ' + str(np.round(pli_passage[1][0],decimals=2)) + ')' )
        plt.legend(prop={'size':15})
    plt.grid()
    #display the points as dots
    if labels is not None:
        cmap, norm = clustering_color_map[colormap]
        label_values = np.unique(labels)
        for i, l in enumerate(label_values):
            p = points[labels == l]
            new_l = labels[labels == l]
            plt.scatter(p[:,0], p[:,1], c=new_l, cmap=cmap, norm=norm, alpha=alpha)
    else:
        plt.scatter(points[:,0], points[:,1])
    #plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig,dpi=300,format='tif', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()


def weighted_scatter_plot(points, pli_passage=None, path_fig=None, title=None,colormap=None,marksize=1, alpha=1):
    '''
    :param points: the b_coordinates of the streamlines in the 2D space (a Nx2 ndarray)
    :param labels: labels assigned to each point after clustering. a (N,) nddarray
    :param pli_passage: the b_coordinates of the knob a (2,) ndarray
    :param path_fig: the path to save the figure, the type of the figure will be determined from the path
    :param title: the title of the figure
    :return: None
    '''
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10,10)
    #ax.set_facecolor('grey')
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        plt.title('Connectivity Space')
    #Label and dimensions of the axes
    plt.xlabel('Pre Central gyral crest  scaled to 100', fontsize=15)
    plt.ylabel('Post Central gyral crest  scaled to 100', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0, 100, 11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(100, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold')
    #trace de la diagonale comme reference de coordonnees
    x = np.linspace(0,100,1000)
    plt.plot(x,x,color='grey')
    if pli_passage is not None:
    #trace de la position  du pli_passage
        plt.plot([0, pli_passage[0]], [pli_passage[1], pli_passage[1]], 'r:', linewidth=2, alpha=1)
        plt.plot([pli_passage[0], pli_passage[0]], [0, pli_passage[1]], 'r:', linewidth=2, alpha=1)
        plt.scatter([pli_passage[0]], [pli_passage[1]], marker='+', color='red', s=150, label="Pli de Passage")
        plt.legend()
    plt.grid()
    unique_points, weight = np.unique(points,axis=0,return_counts=True)
    plt.scatter(unique_points[:,0],unique_points[:,1],c=weight,s=marksize, alpha=alpha)
    plt.colorbar()
    plt.clim(0,100)
    #plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig, bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()


def density_plot_group(X, Y, density, pli_passage=None, path_fig=None, title=None, nb_levels=150,vmin=None, vmax=None):
    #figure setting
    # figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass
        #plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Precentral gyral crest  scaled to 100', fontsize=15)
    plt.ylabel('Postcentral gyral crest  scaled to 100', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0, 100, 11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.text(-20, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(100, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-20, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')

    if vmin is not None and vmax is not None:
        plt.contourf(X, Y, density, nb_levels, cmap=cm.magma_r,vmin=vmin, vmax=vmax)
        m = plt.cm.ScalarMappable(cmap=cm.magma_r)
        m.set_array(density)
        m.set_clim(vmin, vmax)
        plt.colorbar(m, boundaries=np.linspace(vmin, vmax, nb_levels + 1))
    else:
        #print "bubu"
        plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
        plt.colorbar()
    if pli_passage is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage[0]], [pli_passage[1], pli_passage[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage[0], pli_passage[0]], [0, pli_passage[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage[0]], [pli_passage[1]], marker='+', color='b', s=150, label="PPFM position")
    plt.grid()
    plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig,dpi=300,format='tif',bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass


def density_plot_subject(X, Y, density, pli_passage_subject=None, pli_passage_group=None, path_fig=None, title=None, 
                         nb_levels=100):
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
       pass
       # plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Precentral gyral crest  scaled to 100', fontsize=15)
    plt.ylabel('Postcentral gyral crest  scaled to 100', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0,100, 11))
    plt.yticks(np.linspace(0,100, 11))
    plt.text(-20, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(100, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-20, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')
    plt.grid()
    plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
    m = plt.cm.ScalarMappable(cmap=cm.magma_r)
    m.set_array(density)
    m.set_clim(0, 100)
    cbar = plt.colorbar(m, boundaries=np.linspace(0, 100, 100))
    cbar.set_ticks(np.arange(0, 105, 5))

    plt.clim(0, 100)
    if pli_passage_subject is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_subject[0]], [pli_passage_subject[1], pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_subject[0], pli_passage_subject[0]], [0, pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_subject[0]], [pli_passage_subject[1]], marker='+', color='blue', s=150,
                    label="Individual PPFM  (" + str(np.round(pli_passage_subject[0],decimals=2)) + ' ; ' + str(np.round(pli_passage_subject[1],decimals=2)) + ')' )

    if pli_passage_group is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_group[0]], [pli_passage_group[1], pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_group[0], pli_passage_group[0]], [0, pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_group[0]], [pli_passage_group[1]], marker='+', color='blue', s=150, label="Mean PPFM  (" + str(np.round(pli_passage_group[0],decimals=2)) + ' ; ' + str(np.round(pli_passage_group[1],decimals=2)) + ')')
    plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig,dpi=300,format='tif',bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass


def density_plot_subject_no_annot(X, Y, density, pli_passage_subject=None, pli_passage_group=None, path_fig=None, title=None,
                         nb_levels=100):
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
       pass
       # plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Pre-Central Coordinate', fontsize=15)
    plt.ylabel('Post-Central Coordinate', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0,100, 11))
    plt.yticks(np.linspace(0,100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(90, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')
    plt.grid()
    plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
    #m = plt.cm.ScalarMappable(cmap=cm.magma_r)
    #m.set_array(density)
    #m.set_clim(0, 100)
    #cbar = plt.colorbar(m, boundaries=np.linspace(0, 100, 100))
    #cbar.set_ticks(np.arange(0, 105, 5))

   #plt.clim(0, 100)
    if pli_passage_subject is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_subject[0]], [pli_passage_subject[1], pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_subject[0], pli_passage_subject[0]], [0, pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_subject[0]], [pli_passage_subject[1]], marker='+', color='blue', s=150,
                    label="Individual PPFM  (" + str(np.round(pli_passage_subject[0], decimals=2)) + ' ; ' + str(np.round(pli_passage_subject[1],decimals=2)) + ')' )

    if pli_passage_group is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_group[0]], [pli_passage_group[1], pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_group[0], pli_passage_group[0]], [0, pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_group[0]], [pli_passage_group[1]], marker='+', color='blue', s=150, label="Mean PPFM  (" + str(np.round(pli_passage_group[0],decimals=2)) + ' ; ' + str(np.round(pli_passage_group[1],decimals=2)) + ')')
    plt.legend(prop={'size': 15})
    if path_fig is not None:
        plt.savefig(path_fig, dpi=300, format='tif', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass



def density_plot_subject_no_annot_crests(X, Y, density, pli_passage_subject=None, pli_passage_group=None, path_fig=None, title=None,
                         nb_levels=100):
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
       pass
       # plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Pre-Central Coordinate', fontsize=15,color='xkcd:orange',fontname='Arial')
    plt.ylabel('Post-Central Coordinate', fontsize=15,color='purple',fontname='Arial')
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0,100, 11))
    plt.yticks(np.linspace(0,100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold',fontname='Arial')
    plt.text(90, -7, 'Dorsal', fontsize=15, weight='bold',fontname='Arial')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold',fontname='Arial')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')
    plt.grid()
    plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
    #m = plt.cm.ScalarMappable(cmap=cm.magma_r)
    #m.set_array(density)
    #m.set_clim(0, 100)
    #cbar = plt.colorbar(m, boundaries=np.linspace(0, 100, 100))
    #cbar.set_ticks(np.arange(0, 105, 5))

   #plt.clim(0, 100)
    plt.arrow(x=0, y=0, dx=100, dy=0, color='xkcd:orange', linewidth=10)
    plt.arrow(x=0, y=0, dx=0, dy=100, color='purple', linewidth=10)

    plt.plot([30, 30], [0, 60], color='xkcd:orange',linestyle='--', linewidth=2, alpha=1)
    plt.plot([0, 30], [60, 60], color='purple',linestyle='--', linewidth=2, alpha=1)

    plt.plot([45, 30], [45, 60], color='dodgerblue', linestyle='--', linewidth=2, alpha=1)
    #plt.plot([-15, 30], [15, 60], color='fuchsia', linestyle='--', linewidth=2, alpha=1)
    #plt.plot([0, 30], [60, 60], color='purple', linestyle='--', linewidth=2, alpha=1)
    plt.arrow(x=0, y=0, dx=100, dy=100, color='dodgerblue', linewidth=5)
    plt.arrow(x=0,y=0,dx=-50,dy=50, color='fuchsia', linewidth=10)

    plt.scatter([30], [60], marker='+', color='black', s=150)
    ax.annotate('', xy=(-0.5, 0.5), xycoords='axes fraction', xytext=(0, 0),
                arrowprops=dict(arrowstyle="simple", color='fuchsia',linewidth=4))
    #ax.annotate('', xy=(-0.15, 0.15), xycoords='axes fraction', xytext=(0.3, 0.6),
                #arrowprops=dict(arrowstyle="default", color='fuchsia', linewidth=2, linestyle='--'))
    plt.text(35, 30, 'Diagonal Coordinate (Diag_C)', fontsize=15, fontname='Arial',rotation=45, color='dodgerblue')
    #plt.text(-20, 15, 'Orthogonal Coordinate (Orth_C)', fontsize=15, fontname='Arial', rotation=135, color='fuchsia')




    if pli_passage_subject is not None:
        # trace de la position  du pli_passage
        #plt.plot([0, pli_passage_subject[0]], [pli_passage_subject[1], pli_passage_subject[1]], 'b--', linewidth=2, alpha=1)
        #plt.plot([pli_passage_subject[0], pli_passage_subject[0]], [0, pli_passage_subject[1]], 'b--', linewidth=2, alpha=1)
        plt.scatter([pli_passage_subject[0]], [pli_passage_subject[1]], marker='o', color='blue', s=150,
                    label="Individual PPFM  (" + str(np.round(pli_passage_subject[0], decimals=2)) + ' ; ' + str(np.round(pli_passage_subject[1],decimals=2)) + ')' )

    if pli_passage_group is not None:
        # trace de la position  du pli_passage

        plt.plot([0, pli_passage_group[0]], [pli_passage_group[1], pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_group[0], pli_passage_group[0]], [0, pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_group[0]], [pli_passage_group[1]], marker='+', color='blue', s=150, label="Mean PPFM  (" + str(np.round(pli_passage_group[0],decimals=2)) + ' ; ' + str(np.round(pli_passage_group[1],decimals=2)) + ')')

    plt.legend(prop={'size': 15})
    if path_fig is not None:
        plt.savefig(path_fig, dpi=300, format='tif', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass

def plot_ellipse(ax, mu, sigma, color="k"):
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

    #ax.tick_params(axis='both', which='major', labelsize=20)
    ellipse = Ellipse(mu, w, h, theta, fill=False,edgecolor=color,linewidth=4)  # color="k")
    #ellipse.set_clip_box(ax.bbox)
    ellipse.set_alpha(1)
    ax.add_patch(ellipse)
    ax.scatter(mu[0],mu[1],s=150, marker='+',color=color)
    return ax

def density_and_clusters_ellipses(X, Y, density,means,covariances, pli_passage = None, path_fig = None, title = None, \
                                                                                                      nb_levels = \
    100, vmin=None, vmax=None):

    # figure setting
    # figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass

    # Label and dimensions of the axes
    plt.xlabel('Pre-Central Coordinate', fontsize=15)
    plt.ylabel('Post-Central Coordinate', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0, 100, 11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(90, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    ax.plot(x, x, color='grey')
    plt.grid()
    if vmin is not None and vmax is not None:
        ax.contourf(X, Y, density, nb_levels, cmap=cm.magma_r, vmin=vmin, vmax=vmax)
        #m = plt.cm.ScalarMappable(cmap=cm.magma_r)
        #m.set_array(density)
        #m.set_clim(vmin, vmax)
        #cbar = plt.colorbar(m, boundaries=np.linspace(vmin, vmax, nb_levels + 1))
        #cbar.set_ticks(np.arange(vmin, vmax + 500, 500))
    else:
        ax.contourf(X, Y, density, nb_levels, cmap='magma_r')
        #plt.colorbar()
    #drawing the ellipses representing clusters
    colors=['red','blue','orange','green','purple']
    for i, m in enumerate(means):
        #print i,  m
        #print i, covariances[i]
        plot_ellipse(ax, m,covariances[i],color=colors[i])
    if pli_passage is not None:
    # trace de la position  du pli_passage
        plt.plot([0, pli_passage[0]], [pli_passage[1], pli_passage[1]], 'b:', linewidth=2, alpha=1)
        plt.plot([pli_passage[0], pli_passage[0]], [0, pli_passage[1]], 'b:', linewidth=2, alpha=1)
        plt.scatter([pli_passage[0]], [pli_passage[1]], marker='+', color='blue', s=150, label="PPFM ")
    #plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig,dpi=300, format='tif', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass






def density_plot_subject_with_maxima(X, Y, density, pli_passage_subject=None, pli_passage_group=None, path_fig=None, title=None,
                         nb_levels=100):
    #figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Precentral gyral crest  scaled to 100', fontsize=15)
    plt.ylabel('Postcentral gyral crest  scaled to 100', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0,100, 11))
    plt.yticks(np.linspace(0,100, 11))
    plt.text(-20, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(100, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-20, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')
    plt.grid()
    plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
    m = plt.cm.ScalarMappable(cmap=cm.magma_r)
    m.set_array(density)
    m.set_clim(0, 100)
    plt.colorbar(m, boundaries=np.linspace(0, 100, 20 + 1))
    plt.clim(0, 100)

    #
    peaks_indexes = peak_local_max(density,3,threshold_rel=0.30,threshold_abs=50,exclude_border=False)
    #print peaks_indexes.shape
    plt.plot(peaks_indexes[:,1], peaks_indexes[:,0], 'g+', markersize=15,mew=2, label='Density`s Local Maxima')


    #plt.clim(0, 300)
    if pli_passage_subject is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_subject[0]], [pli_passage_subject[1], pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_subject[0], pli_passage_subject[0]], [0, pli_passage_subject[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_subject[0]], [pli_passage_subject[1]], marker='+', color='blue', s=150,
                    label="PPFM position")

    if pli_passage_group is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage_group[0]], [pli_passage_group[1], pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage_group[0], pli_passage_group[0]], [0, pli_passage_group[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage_group[0]], [pli_passage_group[1]], marker='+', color='blue', s=150, label="PPFM position ")
    plt.legend()
    if path_fig is not None:
        plt.savefig(path_fig)
        plt.close(fig)
    else:
        plt.show()
    pass



def density_plot_group_with_maxima(X, Y, density, pli_passage=None, path_fig=None, title=None, nb_levels=150,vmin=None, vmax=None):
    #figure setting
    # figure setting
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    if title is not None:
        plt.title(title, fontsize=20)
    else:
        pass
        #plt.title('Connectivity Space')
    # Label and dimensions of the axes
    plt.xlabel('Pre-Central Coordinate', fontsize=15)
    plt.ylabel('Post-Central Coordinate', fontsize=15)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.xticks(np.linspace(0, 100, 11))
    plt.yticks(np.linspace(0, 100, 11))
    plt.text(-15, -7, 'Ventral', fontsize=15, weight='bold')
    plt.text(90, -7, 'Dorsal', fontsize=15, weight='bold')
    plt.text(-15, 100, 'Dorsal', fontsize=15, weight='bold')
    # trace de la diagonale comme reference de coordonnees
    x = np.linspace(0, 100, 1000)
    plt.plot(x, x, color='grey')

    if vmin is not None and vmax is not None:
        plt.contourf(X, Y, density, nb_levels, cmap=cm.magma_r,vmin=vmin, vmax=vmax)
        #m = plt.cm.ScalarMappable(cmap=cm.magma_r)
        #m.set_array(density)
        #m.set_clim(vmin, vmax)
        #cbar = plt.colorbar(m, boundaries=np.linspace(vmin, vmax, nb_levels + 1))
        #cbar.set_ticks(np.arange(vmin,vmax +500, 500 ))

    else:
        #print "bubu"
        plt.contourf(X, Y, density, nb_levels, cmap='magma_r')
        #cbar = plt.colorbar()



    if pli_passage is not None:
        # trace de la position  du pli_passage
        plt.plot([0, pli_passage[0]], [pli_passage[1], pli_passage[1]], 'b', linewidth=2, alpha=1)
        plt.plot([pli_passage[0], pli_passage[0]], [0, pli_passage[1]], 'b', linewidth=2, alpha=1)
        plt.scatter([pli_passage[0]], [pli_passage[1]], marker='+', color='b', s=150, label="Mean PPFM  (" + str(np.round(pli_passage[0],decimals=2)) + ' ; ' + str(np.round(pli_passage[1],decimals=2)) + ')')

    peaks_indexes = peak_local_max(density, 3, threshold_rel=0.30, threshold_abs=0, exclude_border=False)
    # print peaks_indexes.shape
    plt.plot(peaks_indexes[:, 1], peaks_indexes[:, 0], 'gv', markersize=10, mew=0, label="U-fibre Density's Local Maxima")
    plt.grid()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07), fancybox=True, shadow=False, ncol=2,prop={'size':15})
    if path_fig is not None:
        plt.savefig(path_fig,dpi=300,format='tif',bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
    else:
        plt.show()
    pass







