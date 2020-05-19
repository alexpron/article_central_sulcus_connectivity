"""
Streamlines processing module
to be used as supplement of functions provided by dipy.
Note: most of thes functions are deprecated due to updates in Dipy
they are kept here because there were used into this study
"""

import numpy as np
from dipy.tracking.metrics import frenet_serret


###############################################################
# Numpy array version of the functions
def get_start_points(streamlines, n=1):
    ''' Select the first element of the streamlines
    :param streamlines:
    :param n :
    :return:
    '''
    s_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    for i, s in enumerate(streamlines):
        s_points[i] = np.mean(s[:n], axis=0)
    return s_points


def get_start_points_from_generator(streamlines, n=1):
    '''Generator version of the get_start_point function slower but avoid to use too many memory
    because it keeps only start points into memory'''
    return np.array([np.mean(s[:n], axis=0) for s in streamlines])


def get_end_points_from_generator(streamlines, n=1):
    '''Generator version of the get_end_point function slower but avoid to use too many memory
    because it keeps only start points into memory'''
    return np.array([np.mean(s[-n:], axis=0) for s in streamlines])


def get_lengths_from_generator(streamlines):
    return np.array([s.shape[0] for s in streamlines])


def get_end_points(streamlines, n=1):
    '''
    :param streamlines:
    :param n:
    :return:
    '''
    e_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    for i, s in enumerate(streamlines):
        e_points[i] = np.mean(s[-n:], axis=0)
    return e_points


def get_lengths(streamlines):
    '''
    :param streamlines:
    :return: lenght of  streamlines belonging to the bundle
    '''
    length = np.zeros(len(streamlines))
    for i, s in enumerate(streamlines):
        length[i] = np.sum(np.sqrt(np.sum((s[1:] - s[:-1]) ** 2, axis=1)))
    return length


###########################################################
# Aims Mesh version of the functions

def bundle_to_index(bundle):
    '''
    :param bundle: List of Arrays or ArraySequence
    :return: array with the indexes of the different streamlines
    '''
    sizes = np.array([s.shape[0] for i, s in enumerate(bundle)])
    total_sizes = np.sum(sizes)
    cumsizes = np.cumsum(sizes)
    index = np.ones(total_sizes)
    for i, v in enumerate(cumsizes):
        if i == 0:
            index[:cumsizes[i]] = 0
        else:
            index[cumsizes[i - 1]:cumsizes[i]] *= i
    return index


def size(bundle):
    '''
    Return the number of 'points' contained in a bundle.
    This is equal to the sum of the len of the streamlines over the set of streamlines
    :param bundle:
    :return: number of points into the bundle
    '''
    b_size = 0
    for i, s in enumerate(bundle):
        b_size += len(s)
    return b_size


def cumulative_sizes(bundle):
    '''
    Useful function to index results coming from the bundle
    :param bundle:
    :return:
    '''
    sizes = np.array([len(s) for i, s in enumerate(bundle)])
    cumsizes = np.cumsum(sizes)
    return cumsizes


def compute_frenet_serret(bundle, local=False):
    '''Extend frenet Serret invariant function to whole bundle of streamlines
    This is the fastest but greedy version which require to keep in memory the whole bundle '''
    cs = cumulative_sizes(bundle)
    nb_points = cs[-1]
    T = np.zeros((nb_points, 3))
    N = np.zeros((nb_points, 3))
    B = np.zeros((nb_points, 3))
    k = np.zeros((nb_points, 1))
    t = np.zeros(nb_points)
    for i, s in enumerate(bundle):
        T_, N_, B_, k_, t_ = frenet_serret(s)
        if local is False:
            mean_T = np.mean(T_, axis=0)
            T_[:] = mean_T
        if i == 0:
            T[:cs[i]] = T_
            N[:cs[i]] = N_
            B[:cs[i]] = B_
            k[:cs[i]] = k_
            t[:cs[i]] = t_
        else:
            T[cs[i - 1]:cs[i]] = T_
            N[cs[i - 1]:cs[i]] = N_
            B[cs[i - 1]:cs[i]] = B_
            k[cs[i - 1]:cs[i]] = k_
            t[cs[i - 1]:cs[i]] = t_
    return T, N, B, k, t


def compute_frenet_serret_max(bundle):
    '''Extend frenet Serret invariant function to whole bundle of streamlines
    This is the fastest but greedy version which require to keep in memory the whole bundle '''
    cs = cumulative_sizes(bundle)
    nb_points = cs[-1]
    T = np.zeros((nb_points, 3))
    N = np.zeros((nb_points, 3))
    B = np.zeros((nb_points, 3))
    k = np.zeros((nb_points, 1))
    t = np.zeros(nb_points)
    for i, s in enumerate(bundle):
        T_, N_, B_, k_, t_ = frenet_serret(s)
        if i == 0:
            T[:cs[i]] = T_
            N[:cs[i]] = N_
            B[:cs[i]] = B_
            k[:cs[i]] = k_.max()
            t[:cs[i]] = t_.max()
        else:
            T[cs[i - 1]:cs[i]] = T_
            N[cs[i - 1]:cs[i]] = N_
            B[cs[i - 1]:cs[i]] = B_
            k[cs[i - 1]:cs[i]] = k_.max()
            t[cs[i - 1]:cs[i]] = t_.max()
    return T, N, B, k, t


def compute_frenet_serret_min(bundle):
    '''Extend frenet Serret invariant function to whole bundle of streamlines
    This is the fastest but greedy version which require to keep in memory the whole bundle '''
    cs = cumulative_sizes(bundle)
    nb_points = cs[-1]
    T = np.zeros((nb_points, 3))
    N = np.zeros((nb_points, 3))
    B = np.zeros((nb_points, 3))
    k = np.zeros((nb_points, 1))
    t = np.zeros(nb_points)
    for i, s in enumerate(bundle):
        T_, N_, B_, k_, t_ = frenet_serret(s)
        if i == 0:
            T[:cs[i]] = T_
            N[:cs[i]] = N_
            B[:cs[i]] = B_
            k[:cs[i]] = k_.min()
            t[:cs[i]] = t_.min()
        else:
            T[cs[i - 1]:cs[i]] = T_
            N[cs[i - 1]:cs[i]] = N_
            B[cs[i - 1]:cs[i]] = B_
            k[cs[i - 1]:cs[i]] = k_.min()
            t[cs[i - 1]:cs[i]] = t_.min()
    return T, N, B, k, t


def apply_scalar_texture(bundle, scalar_texture):
    ''' One scalar by streamline applied to each point of the streaamline'''
    if len(bundle) == len(scalar_texture):
        sizes = cumulative_sizes(bundle)
        size = sizes[-1]
        texture = np.zeros(size)
        for i, t in enumerate(scalar_texture.tolist()):
            if i == 0:
                texture[:sizes[i]] = t
            else:
                texture[sizes[i - 1]:sizes[i]] = t
        return texture
