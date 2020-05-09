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

    # path_list = os.path.join(DIR_META, 'subjects_list.txt')
    # subjects = read_subjects_list(path_list=path_list)
    subjects = ['129129', '132017', '144125', '147030', '156637', '189450', '196346', '285345', '346137', '432332',
                '571144', '583858', '598568']

    #metadata to lauch cluster
    dir_cluster = os.path.join(DIR_PROJECT,'cluster','distance')
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)

    extremities = ['s','e']

    for sub in subjects:
        path_vertices = os.path.join(DIR_OUT,'gw_interface', 'arrays', sub + '_wm_vertices.npy')
        for ext in extremities:
            path_points = os.path.join(DIR_OUT,'extremities', sub + '_'+ ext +'_points.npy')
            path_index = os.path.join(DIR_OUT,'nearest_mesh_vertex', sub + '_' + ext + '_nearest_vertex.npy')
            
            if os.path.exists(path_points):
                    stderr = os.path.join(dir_cluster,sub + '_' + ext  +'points.stderr')
                    stdout = os.path.join(dir_cluster,sub + '_' + ext  +'points.stdout')
                    cmd_file = os.path.join(dir_cluster,sub + '_' + ext  +'points.cmd')
                    cluster_files = [stderr,stdout,cmd_file]
                    for c in cluster_files:
                            if os.path.exists(c):
                                    os.remove(c)

                    cmd = os.path.join(DIR_PROJECT,'scripts','pipeline','e_nearest_mesh_vertex', 'f_compute_nearest_vertex.py') + '  '  + path_points + '  ' + path_vertices + '  ' + path_index
                    #print cmd
                    os.system('frioul_batch  -c  8 -d ' + dir_cluster + ' -O ' + stdout + ' -E ' + stderr + ' -C ' + cmd_file +  ' " ' + cmd + ' " ' )








