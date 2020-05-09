import os
import numpy as np

def read_subjects_list(path_list):
    subs = np.loadtxt(path_list)
    subjects_list = [str(int(s)) for s in subs]
    return subjects_list


if __name__ == '__main__':

    DIR_PROJECT = '/hpc/meca/users/pron.a/HCP/Central_Sulcus_Connectivity'
    DIR_DATA = os.path.join(DIR_PROJECT, 'data')
    DIR_META = os.path.join(DIR_PROJECT, 'metadata')
    DIR_INPUT = os.path.join(DIR_DATA, 'input')
    DIR_OUT = os.path.join(DIR_DATA, 'output')

    path_list = os.path.join(DIR_META, 'subjects_list.txt')
    #subjects = read_subjects_list(path_list=path_list)



    #metadata to lauch cluster
    dir_cluster = os.path.join(DIR_PROJECT,'cluster','extremities')
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)

    subjects = ['129129', '132017', '144125', '147030', '156637', '189450', '196346', '285345', '346137', '432332', '571144', '583858', '598568']
    for sub in subjects:

        path_trk = os.path.join('/envau/work/meca/data/HCP/data/BV_database/subjects',sub,'dmri','default_acquisition',
                                'HCP_pipeline',
                                'tractography','filtered_tracks.trk')
        path_affine = os.path.join('/envau/work/meca/data/HCP/data/BV_database/subjects',sub,'dmri','default_acquisition',
                                'HCP_pipeline','csd','MSMT', 'brain_fit','wm_fod_RAS_to_aims.npy')
        if (os.path.exists(path_trk) and os.path.exists(path_affine)): #and not os.path.exists(os.path.join(DIR_OUT,'extremities', sub + '_s_points_0.npy')) :
            path_s_points = os.path.join(DIR_OUT,'extremities', sub + '_s_points.npy')
            path_e_points = os.path.join(DIR_OUT, 'extremities', sub + '_e_points.npy')

            stderr = os.path.join(dir_cluster,sub + '.stderr')
            stdout = os.path.join(dir_cluster, sub + '.stdout')
            cmd_file = os.path.join(dir_cluster, sub + '.cmd')

            cmd = os.path.join(DIR_PROJECT,'scripts','pipeline','d_extract_fibers_extremities','extract_streamlines_extremities_cluster.py') + '  ' + \
                  path_trk + '  ' + path_affine + '  ' + path_s_points + '  ' + path_e_points
            print  cmd
            os.system('frioul_batch  -c 4 -d ' + dir_cluster + ' -O ' + stdout + ' -E ' + stderr + ' -C ' + cmd_file
                      +  ' " ' + cmd + ' " ' )








