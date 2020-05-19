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

    for i, side in enumerate(SIDES):
        name = d + '_' + side + '_' + 'n' + '_' + str(n) + '_' + init_method + '_' + 'init' + '_' + str(
            n_init)
        #path_w = os.path.join(dir_output, 'central_cluster', name + '_' + 'weights' + '.npy')
        path_m = os.path.join(dir_output, 'central_cluster', name + '_' + 'means' + '.npy')
        path_c = os.path.join(dir_output, 'central_cluster', name + '_' + 'covariances' + '.npy')

        means = np.load(path_m)
        cov = np.load(path_c)

        #sort means and labels by precentral coordinate
        t = np.argsort(means, axis=0)[:, 0]
        sorted_cov = cov[t]
        sorted_means = means[t]
        #hemisphere data
        data_ = data[side_index == i]

        distances = np.zeros((3,data_.shape[0]))

        for c in range(3):

            mean = sorted_means[c]
            covariance = sorted_cov[c]
            #distance from x --> mean with the inverse covariance matrix of
            distance = cdist(data_,mean[np.newaxis,:],'mahalanobis',VI=np.linalg.inv(covariance))
            #square distance to respect X2 law
            distance = distance**2
            distances[c] = distance[:,0]
        path_distance = os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','mahalanobis' +
                                     '_' + side + '.npy' )
        np.save(path_distance, distances)













