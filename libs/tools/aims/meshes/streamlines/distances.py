import numpy as np
from scipy.spatial.distance import cdist


def streamlines_nearest_vertex(points, vertices, size_chunk=10000):
    """
    Small hack to avoid memory error even on the cluster. This function acts as a compromise
    between performance and memory consumption. Since (N1,N) distance array can generally not be created on cluster
    this function split it into several parts (in the streamlines domain)
    :param points: extremities of the streamlines (or mean extremities) (N,3) array
    :param vertices:  (N1,3) array
    :param size_chunk: size of the sub array to be considered
    :return:nearest_vertices (N,3) array containing the index of the nearest vertices for the euclidian distance
    """
    nb_points = len(points)
    nb_chunk = int(nb_points) / int(size_chunk) + 1
    nearest_vertices = np.zeros(nb_points, dtype=np.int)
    for i in range(nb_chunk):
        n_min = i * size_chunk
        n_max = min((i + 1) * size_chunk, len(points))
        n_points = points[n_min:n_max]
        distances = cdist(n_points, vertices)
        nearest_vertices[n_min:n_max] = np.argmin(distances, axis=1)
    return nearest_vertices


def fibers_index_by_vertex(nearest_vertex_index, nb_vertices):
    """
    :param nearest_vertex_index:
    :param nb_vertices:
    :return:
    """
    hist, edges = np.histogram(nearest_vertex_index, bins=np.arange(nb_vertices + 1))
    del edges
    index = []
    for i in range(nb_vertices):
        if hist[i] == 0:
            a = np.array([])
            index.append(a)
        else:
            a = np.where(nearest_vertex_index == i)[0]
            index.append(a)
    final_index = np.array(index, dtype=object)
    return final_index


def full_fibers_index_by_vertex(s_vertex_index, e_vertex_index, nb_vertices):
    hist_s, edges = np.histogram(s_vertex_index, bins=np.arange(nb_vertices + 1))
    hist_e, edges = np.histogram(e_vertex_index, bins=np.arange(nb_vertices + 1))
    del edges
    hist = hist_s + hist_e
    index = []
    for i in range(nb_vertices):
        if hist[i] == 0:
            a = np.array([])

        else:
            if hist_s[i] == 0:
                a = np.where(e_vertex_index == i)[0]
            if hist_e[i] == 0:
                a = np.where(s_vertex_index == i)[0]
            else:
                a = np.unique(
                    np.concatenate(
                        (
                            np.where(s_vertex_index == i)[0],
                            np.where(e_vertex_index == i)[0],
                        )
                    )
                )
        index.append(a)
    final_index = np.array(index, dtype=object)
    return final_index


def compute_vertex_density(s_vertex, e_vertex, nb_vertices):
    """This function compute at each vertex a so called vertex
    connectivity_profiles i.e the number of the streamlines at the node divided by
    the total number of streamlines. This is not a surfacic connectivity_profiles"""
    nb_fibers = s_vertex.shape[0]
    index_vertices = np.arange(nb_vertices + 1).astype(int)
    density = np.zeros(nb_vertices)
    # index des fibres bouclant sur un vertex
    index_boucling = np.where(s_vertex == e_vertex)
    index_diff = np.where(s_vertex != e_vertex)
    # on compte separement les fibres bouclant pour ne pas les compter deux fois
    if len(index_boucling[0]) > 0:
        boucling_vertices = s_vertex[index_boucling].astype(int)
        u_vertices = np.unique(boucling_vertices)
        for b in u_vertices:
            density[b] = len(boucling_vertices[boucling_vertices == b])
    # les fibres ne bouclant pas peuvent etre sommees directement
    points = np.concatenate(s_vertex[index_diff], e_vertex[index_diff])
    hist, bins = np.histogram(points, bins=index_vertices)
    density += hist
    density /= nb_fibers
    return density
