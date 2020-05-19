import os
import numpy as np
from variables import SUBJ_LIST, SIDES, DIR_OUT


if __name__ == '__main__':

    d = 'global_mean'
    n = 3
    n_init = 1000
    max_iter = 5000
    init_method = 'kmeans'
    #threshold = 9.2103
    threshold = 13.8155# alpha=0.01 significant level of the CHi2 distribution
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')

    path_data = os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'length_filtered', 'U_fibers_coord' + '_' + d +
                             '.npy')
    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index_filtered.npy')
    data = np.load(path_data)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index, 2)
    for i, side in enumerate(SIDES):
        name = d + '_' + side + '_' + 'n' + '_' + str(n) + '_' + init_method + '_' + 'init' + '_' + str(
            n_init)
        path_central_cluster_labels = os.path.join(dir_output, d + '_' + 'all_labels' + '_' + side + '.npy')
        path_labels = os.path.join(dir_output, d + '_' + 'whole_hemisphere_all_labels' + '_' + side + '.npy')
        path_mah_distance = os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','mahalanobis' +
                                     '_' + side + '.npy')
        init_labels = np.load(path_central_cluster_labels)
        whole_space_labels = np.load(path_labels)
        dist = np.load(path_mah_distance)
        data_ = data[side_index == i]
        #build mask (+ is equivalent to or)
        a ,b ,c = dist[0]<threshold , dist[1]<threshold , dist[2]<threshold
        mask = a + b + c
        spread_labels = init_labels.copy()
        spread_labels[mask] = whole_space_labels[mask]
        np.save(os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','clusters', side + '.npy'),
                spread_labels)












