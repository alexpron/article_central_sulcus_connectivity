import os


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST
    #metadata to lauch cluster
    dir_cluster = os.path.join(DIR_PROJECT,'cluster','extremities')
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)


    for subject in SUBJ_LIST:


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








