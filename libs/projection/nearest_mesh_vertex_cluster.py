#!/hpc/meca/users/pron.a/softs/brainvisa-4.6.1/bin/python -u

from scipy.spatial.distance import cdist
from soma import aims
import numpy as np
import sys


def streamlines_nearest_vertex(points, vertices, size_chunk=10000):
    '''
    Small hack to avoid memory error even on the cluster. This function acts as a compromise
    between performance and memory consumption. Since (N1,N) distance array can generally not be created on cluster
    this function split it into several parts (in the fibers domain)
    :param points: extremities of the fibers (or mean extremities) (N,3) array
    :param vertices:  (N1,3) array
    :param size_chunk: size of the sub array to be considered
    :return:nearest_vertices (N,3) array containing the index of the nearest vertices for the euclidian distance
    '''
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


def main(path_points, path_mesh, path_index):
    points = np.load(path_points)
    vertices = np.array(aims.read(path_mesh).vertex())
    n_vertices = streamlines_nearest_vertex(points, vertices)
    np.save(path_index, n_vertices)
    pass


if __name__ == '__main__':
    args = sys.argv
    path_points = args[1]
    path_vertices = args[2]
    path_index = args[3]
    main(path_points, path_vertices, path_index)
