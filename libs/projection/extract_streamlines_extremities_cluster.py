#!/hpc/meca/users/pron.a/softs/brainvisa-4.6.1/bin/python -u

import nibabel as nib
import sys
import numpy as np

def load_trk_aims_space(path_trk_file,path_affine,lazy=False):
    '''Load streamlines b_coordinates into Aims mm space to be coherent
    with computation and visualization done into both Aims and Anatomist:
    Remark if lazy=True the streamlines return is a generator object (in order not
    to overload memory. A streamlines = list(streamlines) call should be done
    to actually retrieved streamlines b_coordinates'''

    affine = np.load(path_affine)
    trkfile = nib.streamlines.load(path_trk_file, lazy_load=lazy)
    tractogram = trkfile.tractogram
    #by default streamlines are loaded into RAS mm space
    #retrieving affine transformation and putting them into RAS space

    new_tractogram = tractogram.apply_affine(affine)
    #put streamlines into AIMS mm space
    streamlines = new_tractogram.streamlines
    return streamlines


def get_extremities_points(streamlines,n=1):
    '''
    :param streamlines:
    :param n:
    :return:
    '''
    s_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    e_points = np.zeros((len(streamlines), streamlines[0][0].shape[-1]))
    for i, s in enumerate(streamlines):
        s_points[i] = np.mean(s[:n],axis=0)
        e_points[i] = np.mean(s[-n:], axis=0)
    return s_points, e_points




if __name__ == '__main__':

    args = sys.argv
    path_trk = args[1]
    path_affine = args[2]
    path_s_points = args[3]
    path_e_points = args[4]

    streamlines = load_trk_aims_space(path_trk,path_affine)
    s_points, e_points = get_extremities_points(streamlines)
    np.save(path_s_points, s_points)
    np.save(path_e_points, e_points)
