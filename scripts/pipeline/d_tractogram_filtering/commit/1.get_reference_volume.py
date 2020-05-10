from soma import aims
import numpy as np
import os
#from tools.tools import read_subjects_list

def get_aims_to_RAS_transfo(path_volume,path_transformation):
    '''Retrieve the estimated transformation between AIMS mm and RAS mm space'''
    vol = aims.read(path_volume)
    aims_to_RAS = aims.AffineTransformation3d(vol.header()['transformations'][0])
    RAS_to_aims = aims_to_RAS.inverse()
    aff = np.array(aims_to_RAS.toMatrix())
    print aff
    affine = np.array(RAS_to_aims.toMatrix())
    print affine
    np.save(path_transformation,affine)
    return affine

#TO DO : underestand why import does not work

def read_subjects_list(subjects_list_path):
    '''
    Return the subjects ids as a list of string
    :param subjects_list_path:
    :return:
    '''
    sub_list = np.loadtxt(subjects_list_path)
    subj_list = sub_list.astype(int)
    subject_list = [str(s) for s in subj_list]
    return subject_list


if __name__ == '__main__':

    HCP_db = os.environ["HCP_DATASET"]
    BV_db = os.environ["BV_DB"]
    dwi_acq = os.environ["DWI_ACQ"]
    dwi_proc = os.environ["DWI_PROC"]
    subjects_list = read_subjects_list(os.environ['SUBJ_LIST'])


    for sub in subjects_list:
        path_reference_volume = os.path.join(BV_db,sub,'dmri',dwi_acq,dwi_proc,'csd','MSMT','brain_fit','wm_fod.nii.gz')
        path_affine = os.path.join(BV_db,sub,'dmri',dwi_acq,dwi_proc,'csd','MSMT','brain_fit','wm_fod_RAS_to_aims.npy')
        get_aims_to_RAS_transfo(path_reference_volume,path_affine)






