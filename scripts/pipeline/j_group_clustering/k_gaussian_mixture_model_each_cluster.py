import numpy as np
import os
from sklearn.mixture.gaussian_mixture import GaussianMixture
from variables import DIR_OUT, DIR_DATA, SIDES


if __name__ == '__main__':
    #density with aligned knob
    d = 'global_mean'
    path_data = os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'length_filtered', 'U_fibers_coord' + '_' + d +
                             '.npy')
    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index_filtered.npy')
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')
    path_labels = os.path.join(dir_output,  d + '_' + 'labels' + '.npy')


    data = np.load(path_data)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index, 2)
    labels = np.load(path_labels)

    #remove noise
    labels_clean = labels[labels!=-1]
    side_index_clean = side_index[labels!=-1]
    data_clean = data[labels!=-1]

    #parameters used for GMM
    n = 5
    n_init = 1000
    max_iter = 5000
    init_method = 'kmeans'
    g = GaussianMixture(n_components=n, n_init=n_init, init_params=init_method, max_iter=max_iter)

    for j, side in enumerate(SIDES):
        name = d + '_' + side + '_' + 'n' + '_' + str(n) + '_' + init_method + '_' +'init' + '_' + str(
            n_init)

        path_data_ = os.path.join(dir_output, 'all_clusters', d + '_' + side + '_' + 'coord' + '.npy')
        path_w = os.path.join(dir_output, 'all_clusters', name + '_' + 'weights' + '.npy')
        path_m = os.path.join(dir_output, 'all_clusters', name + '_' + 'means' + '.npy')
        path_c = os.path.join(dir_output,  'all_clusters', name + '_' + 'covariances' + '.npy')
        path_l = os.path.join(dir_output, 'all_clusters', name + '_' + 'labels' + '.npy')
        path_final_labels = os.path.join(dir_output, d + '_' + 'all_clusters_all_labels' + '_' + side + '.npy')

        # select hemisphere
        data_h = data[side_index==j]
        data_ = data_clean[side_index_clean == j]
        labels_ = labels_clean[side_index_clean == j]

        g.fit(data_)
        w = g.weights_
        m = g.means_
        c = g.covariances_
        pred_labels = g.predict(data_h)

        #directly sort the labels according to the precentral coordinates of the cluster
        t = np.argsort(m, axis=0)[:, 0]
        sorted_means = m[t]
        sorted_cov = c[t]
        sorted_weigth = w[t]
        sorted_pred_labels = pred_labels.copy()

        for z, s in enumerate(t):
            # s+1 to account for the existence of ventral cluster
            sorted_pred_labels[pred_labels == s] = z


        np.save(path_data_, data_)
        np.save(path_m, sorted_means)
        np.save(path_w, sorted_weigth)
        np.save(path_c, sorted_cov)
        np.save(path_l, sorted_pred_labels)
        np.save(path_final_labels,sorted_pred_labels)






