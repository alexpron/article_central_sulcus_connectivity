import os
import numpy as np




if __name__ == '__main__':


    dir_cluster = os.path.join(DIR_CLUSTER,'distance')
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)



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








