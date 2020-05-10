import os
from sub_tracks import  extract_sub_tractogram



if __name__ == '__main__':

    HCP_db = os.environ["HCP_DATASET"]
    BV_db = os.environ["BV_DB"]
    dwi_acq = os.environ["DWI_ACQ"]
    dwi_proc = os.environ["DWI_PROC"]
    #subjects_list = read_subjects_list(os.environ["SUBJ_LIST"])
    dir_scripts = os.environ["DIR_SCRIPTS"]
    #dir_cluster = os.path.join(os.environ["DIR_CLUSTER"],'tracks_extraction')
    
    #print dir_cluster
    subjects_list= ['144125', '346137', '196346', '598568', '147030','432332', '129129', '285345', '571144',
              '156637', '583858', '132017','189450']
    for sub in subjects_list:
        #path_tck = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'tractography', 'tracks.tck')
        path_trk = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'tractography', 'tracks.trk')
        path_trk_filtered = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'tractography', 'filtered_tracks.trk')
        path_commit_weight = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'a_commit', 'Results_StickZeppelinBall','results.pickle')

        if os.path.exists(path_trk) and os.path.exists(path_commit_weight) and not os.path.exists(path_trk_filtered):
            #print "ok"
            print sub
            extract_sub_tractogram(path_trk, path_commit_weight,path_trk_filtered)
    pass






