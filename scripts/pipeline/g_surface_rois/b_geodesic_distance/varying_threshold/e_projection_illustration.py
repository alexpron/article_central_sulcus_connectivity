import os
from soma import aims, aimsalgo
import numpy as np
from variables import SUBJ_LIST, SIDES, GYRI,DIR_OUT




if __name__ == '__main__':

    threshold_factor = 1
    SUBJ_LIST = ['114621']

    for i, subject in enumerate(SUBJ_LIST):
        path_mesh = os.path.join(DIR_OUT, 'gw_interface', 'meshes', subject + '.gii')
        mesh = aims.read(path_mesh)
        for j, side in enumerate(SIDES):
            for k, gyri in enumerate(GYRI):
                #Gyral line indexes
                path_gyral_line = os.path.join(DIR_OUT,'gyral_crests', subject + '_' + side + '_' + gyri + '.npy')
                gyral_line = np.load(path_gyral_line)
                gyral_line = gyral_line.tolist()
                path_gyral_param = os.path.join(DIR_OUT,'gyral_crests', subject + '_' + side + '_' + gyri + '_iso_param.npy')
                gyral_param = np.load(path_gyral_param)
                #Threshold on the geodesic dist
                geo_dist_threshold = np.load(os.path.join(DIR_OUT,'geodesic_distances','adaptive_threshold', subject + '_' + side + '_' + gyri + '.npy'))
                geo_dist_threshold*=threshold_factor
                print geo_dist_threshold
                #Geodesic distance map
                geo_dist_t = aims.read(os.path.join(DIR_OUT,'geodesic_distances','raw', subject + '_' + side + '_' +
                                             'distance_to_' + gyri + '.gii'))
                geo_dist = np.array(geo_dist_t[0])
                #Mesh partitionned by geodesic distance
                partition_t = aims.read(os.path.join(DIR_OUT,'geodesic_distances','partitions', subject + '_' + side + '_' + gyri + '.gii'))
                partition = np.array(partition_t[0])
                #just to be sure
                partition_correct_index = partition.copy()
                partition_correct_index = partition_correct_index.astype(np.float32)
                partition_correct_index[partition_correct_index==0]=-1




                #Output texture
                roi = np.zeros(len(geo_dist),dtype=np.uint32)

                for l, g in enumerate(gyral_line):
                    roi[(partition == g)*(geo_dist<=geo_dist_threshold[l])] = 1
                    partition_correct_index[(partition == g) * (geo_dist > geo_dist_threshold[l])] = -1
                    partition_correct_index[(partition == g)*(geo_dist<=geo_dist_threshold[l])] = gyral_param[l]



                roi_t = aims.TimeTexture(partition_correct_index)

                aims.write(roi_t, os.path.join(DIR_OUT,'geodesic_distances','f_projection',subject + '_' + side + '_' + gyri + '.gii'))




























