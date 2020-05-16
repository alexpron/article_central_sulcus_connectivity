import numpy as np
from soma import aims
import nibabel as nib



def select_association_streamline(path_mask, path_affine_dwi_to_t1, path_tractogram, path_association_streamlines):
    """
    :param path_mask:
    :param path_affine_dwi_to_t1:
    :param path_tractogram:
    :param path_association_streamlines:
    :return:
    """
    mask_vol = aims.read(path_mask)
    mask = np.array(mask_vol)[..., 0]
    mask = mask.astype(bool)
    scaling = np.diag(mask_vol.header()['voxel_size'] + [1])
    inv_scaling = np.linalg.inv(scaling)
    dwi_2_t1 = np.array(aims.read(path_affine_dwi_to_t1).toMatrix())
    affine = np.dot(inv_scaling, dwi_2_t1)
    association_streamlines = []
    streamlines = np.load(path_tractogram)
    for streamline in streamlines:
        t1_streamline = nib.affines.apply_affine(affine, streamline)
        status = True
        for v in t1_streamline:
            v1 = v.astype(int)
            status = status * mask[v1[0], v1[1], v1[2]]
        if status:
            association_streamlines.append(streamline)
    association_streamlines = np.array(association_streamlines, dtype=object)
    np.save(path_association_streamlines, association_streamlines)



if __name__ == '__main__':

    from configuration.configuration import TRACTS













#

