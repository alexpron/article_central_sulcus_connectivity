#!/hpc/meca/users/pron.a/softs/brainvisa-4.6.1/bin/python -u

import sys
import numpy as np


def get_extremities_points(streamlines, n=1):
    """
    :param streamlines:
    :param n:
    :return:
    """
    s_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    e_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    for i, s in enumerate(streamlines):
        s_points[i] = np.mean(s[:n], axis=0)
        e_points[i] = np.mean(s[-n:], axis=0)
    return s_points, e_points


if __name__ == "__main__":
    args = sys.argv
    path_tracts = args[1]
    path_affine = args[2]
    path_s_points = args[3]
    path_e_points = args[4]

    streamlines = np.load(path_tracts)
    s_points, e_points = get_extremities_points(streamlines)
    np.save(path_s_points, s_points)
    np.save(path_e_points, e_points)
