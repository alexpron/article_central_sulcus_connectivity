from tractography.commit.commit_filtering import commit_filtering
import os
import numpy as np

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
    path_list = '/envau/work/meca/data/Datasets/HCP/subjects_list.txt'
    #subjects = read_subjects_list(path_list)
    bv_db = '/hpc/meca/data/U_Fibers/BV_database/subjects'
    dwi_acq = 'default_acquisition'
    dwi_proc = 'HCP_pipeline'

    subjects=['144125', '346137', '196346', '598568', '147030','432332', '129129', '285345', '571144',
              '156637', '583858', '132017','189450']
    for i, sub in enumerate(subjects):
        path_trk = os.path.join(bv_db,sub,'dmri',dwi_acq,dwi_proc,'tractography','tracks.trk')
        path_result = os.path.join(bv_db,sub,'dmri',dwi_acq,dwi_proc,'commit','Results_StickZeppelinBall','results.pickle')
        if os.path.exists(path_trk) and not os.path.exists(path_result):
            print "processing", sub
            commit_filtering(sub)
