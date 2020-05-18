import os
import numpy as np
from libs.tools.cluster import launch_subject_cmd


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, DIR_PROJECT, DIR_CLUSTER, MESHES, TRACTS_EXTREMITIES, ASSO_TRACT_EXTREMITIES, ASSO_TRACT_NEAREST_VERTEX

    dir_cluster = os.path.join(DIR_CLUSTER, 'distance')
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)

    for subject in SUBJ_LIST:
        for side in SIDES.keys():
            for ext in TRACTS_EXTREMITIES:
                if os.path.exists(ASSO_TRACT_EXTREMITIES):
                        # TO DO find a way to have relative path so that it works without specifiying absolute path
                        cmd = os.path.join(DIR_PROJECT, 'libs', 'projection', 'nearest_mesh_vertex_cluster.py') + '  ' + ASSO_TRACT_EXTREMITIES[(subject, side, ext)] + '  ' + MESHES[(subject, side, 'white')] + '  ' + ASSO_TRACT_NEAREST_VERTEX[(subject, side, ext)]
                        launch_subject_cmd(cmd, subject + '_' + side, dir_cluster, core=8)









