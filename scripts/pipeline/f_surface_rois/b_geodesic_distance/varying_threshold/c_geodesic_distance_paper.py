import os
from soma import aims, aimsalgo
import numpy as np
from variables import SUBJ_LIST, SIDES, GYRI,DIR_OUT


def adaptative_distance(gyral_line, sulcal_line, mesh):
    geo = aims.GeodesicPath(mesh,0,0)
    indexes = np.zeros(len(gyral_line),dtype=int)
    geo_dist = np.zeros(len(gyral_line),dtype=np.float32)
    for i, g in enumerate(gyral_line):
        index, length  = geo.shortestPath_1_N_ind(g, sulcal_line)
        #print length, index
        geo_dist[i] = length
    return geo_dist



if __name__ == '__main__':

    SUBJ_LIST = ['114621']

    for i, subject in enumerate(SUBJ_LIST):
        path_mesh = os.path.join(DIR_OUT, 'gw_interface', 'meshes', subject + '.gii')
        mesh = aims.read(path_mesh)
        for j, side in enumerate(SIDES):
            path_sulcal_line = os.path.join(DIR_OUT,'sulci','fundus', subject + '_' + side + '.gii')
            sulcal_line_t = aims.read(path_sulcal_line)
            sulcal_line = np.array(sulcal_line_t[0])
            sulcal_line_indexes = np.where(sulcal_line!=0)[0]
            sulcal_line_indexes = sulcal_line_indexes.tolist()
            for k, gyri in enumerate(GYRI):
                path_gyral_line = os.path.join(DIR_OUT,'gyral_crests', subject + '_' + side + '_' + gyri + '.npy')
                gyral_line = np.load(path_gyral_line)
                gyral_line = gyral_line.tolist()
                distance = adaptative_distance(gyral_line,sulcal_line_indexes,mesh)
                np.save(os.path.join(DIR_OUT,'geodesic_distances','adaptive_threshold',subject + '_' + side + '_' + gyri + '.npy'),distance)
























