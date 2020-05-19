import os
import numpy as np
from scipy.spatial.distance import cdist
from scipy.stats._multivariate import multivariate_normal
from matplotlib import pyplot as plt
from variables import SIDES, DIR_OUT
from matplotlib import pyplot as plt

if __name__ == '__main__':

    d = 'global_mean'
    n = 3
    n_init = 1000
    max_iter = 5000
    init_method = 'kmeans'
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')

    data = np.load(os.path.join(DIR_OUT,'connectivity','coordinates','length_filtered','U_fibers_coord_global_mean.npy'))
    hemispheres_index = np.load(os.path.join(DIR_OUT,'connectivity','indexes','hemispheres_index_filtered.npy'))
    side_index = np.mod(hemispheres_index, 2)

    for j, side in enumerate(SIDES):
        name = d + '_' + side + '_' + 'n' + '_' + str(n) + '_' + init_method + '_' +'init' + '_' + str(
            n_init)

        path_m = os.path.join(dir_output, 'all_clusters', name + '_' + 'means' + '.npy')
        path_c = os.path.join(dir_output,  'all_clusters', name + '_' + 'covariances' + '.npy')
        path_l = os.path.join(dir_output, 'all_clusters', name + '_' + 'labels' + '.npy')
        path_labels = os.path.join(dir_output, d + '_' + 'all_clusters_all_labels' + '_' + side + '.npy')

        #hemisphere data
        means = np.load(path_m)
        covs = np.load(path_c)
        labels = np.load(path_labels)
        data_ = data[side_index == j]

        distances = np.zeros((3,data_.shape[0]))

        for c in range(3):
            mean = means[c]
            covariance = covs[c]
            #distance from x --> mean with the inverse covariance matrix of
            distance = cdist(data_,mean[np.newaxis,:],'mahalanobis',VI=np.linalg.inv(covariance))
            #square distance to respect X2 law
            distance = distance**2
            distances[c] = distance[:,0]
        path_distance = os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','mahalanobis' +
                                     '_' + 'all_clusters' + side + '.npy' )
        np.save(path_distance, distances)













