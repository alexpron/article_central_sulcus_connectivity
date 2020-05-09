import nibabel as nib
import numpy as np


def load_trk_aims_space(path_trk_file,path_affine,lazy=True):
    '''Load streamlines coordinates into Aims mm space to be coherent
    with computation and visualization done into both Aims and Anatomist:
    Remark if lazy=True the streamlines return is a generator object (in order not
    to overload memory. A streamlines = list(streamlines) call should be done
    to actually retrieved streamlines coordinates'''

    affine = np.load(path_affine)
    trkfile = nib.streamlines.load(path_trk_file,lazy_load=lazy)
    tractogram = trkfile.tractogram
    #by default streamlines are loaded into RAS mm space
    #retrieving affine transformation and putting them into RAS space

    new_tractogram = tractogram.apply_affine(affine)
    #put streamlines into AIMS mm space
    streamlines = new_tractogram.streamlines
    return streamlines