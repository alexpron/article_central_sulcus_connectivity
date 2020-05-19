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
    THRESH = 9.2103
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
        print data_.shape
        distances = np.load(os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','mahalanobis' +
                                     '_' + side + '.npy' ))
        print distances.shape
        #THRESHOLD is 9.2103 --> Xi2 with 2 dof

        for c in range(3):
            dist = distances[c]
            print dist.shape

            ok_c = dist[dist<THRESH]
            ok_data = data_[dist<THRESH]
            fig, ax = plt.subplots()
            plt.scatter(ok_data[:,0],ok_data[:,1],c=ok_c,s=1)
            plt.colorbar()
            plt.show()
















