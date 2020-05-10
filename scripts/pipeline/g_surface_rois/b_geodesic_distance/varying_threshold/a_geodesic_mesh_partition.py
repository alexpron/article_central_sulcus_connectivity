import os
from soma import aims, aimsalgo
import numpy as np
from variables import SUBJ_LIST, SIDES, GYRI,DIR_OUT




def partition_mesh(line, mesh,roi):
    """
    Create a partition of a mesh such as each vertex of the mesh is associated to its closest point belonging
    to a line drawn onto the mesh
    :param line: sorted np.array
    :param mesh:
    :param surf_roi:
    :return:
    """
    geo = aims.GeodesicPath(mesh, 0, 0)
    vertices = np.array(mesh.vertex())
    partition = -1 * np.ones(vertices.shape[0], dtype=int)
    if roi is not None:
        roi_indexes = np.where(roi != 0)[0].tolist()
    else:
        roi_indexes = np.arange(vertices.shape[0],dtype=int).tolist()
    for i, vertex in enumerate(roi_indexes):
        index, length = geo.shortestPath_1_N_ind(vertex, line)
        partition[vertex] = index
    return partition


if __name__ == '__main__':

    SUBJ_LIST = ['114621']
    for i, subject in enumerate(SUBJ_LIST):
        path_mesh = os.path.join(DIR_OUT, 'gw_interface', 'meshes', subject + '.gii')
        path_hemi_index = os.path.join(DIR_OUT,'gw_interface','meshes',subject + '_' + 'hemi_index.gii')
        mesh = aims.read(path_mesh)
        hemi_index_t = aims.read(path_hemi_index)
        hemi_index = np.array(hemi_index_t[0])
        for j, side in enumerate(SIDES):
            for k, gyri in enumerate(GYRI):
                print subject, side, gyri
                path_geodesic_distance = os.path.join(DIR_OUT, 'geodesic_distances','raw', subject + '_' + side + '_' + 'distance_to_' + gyri + '.gii')
                geodesic_distance_t = aims.read(path_geodesic_distance)
                geodesic_distance = np.array(geodesic_distance_t[0])
                roi = np.zeros_like(geodesic_distance)
                roi[geodesic_distance<30]=1
                path_gyral_line = os.path.join(DIR_OUT,'gyral_crests', subject + '_' + side + '_' + gyri + '.npy')
                gyral_line = np.load(path_gyral_line)
                gyral_line = gyral_line.tolist()
                partition = partition_mesh(gyral_line,mesh,roi)
                np.save(os.path.join(DIR_OUT,'geodesic_distances','partitions', subject + '_' + side + '_' + gyri + '.npy'),partition)

















