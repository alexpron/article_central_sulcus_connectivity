import numpy as np
from sklearn.mixture.gaussian_mixture import GaussianMixture

if __name__ == '__main__':

    from configuration.configuration import SIDES, U_FIBERS_COORD, HEMI_INDEXES, DBSCAN_LABELS, N, N_INIT, INIT_METHOD, \
        CLUSTERING_LABELS

    data = np.load(U_FIBERS_COORD['global_mean'])
    hemispheres_index = np.load(HEMI_INDEXES)
    side_index = np.mod(hemispheres_index, 2)
    labels = np.load(DBSCAN_LABELS)
    g = GaussianMixture(n_components=N, n_init=N_INIT, init_params=INIT_METHOD)
    for j, side in enumerate(SIDES.keys()):

        data_ = data[side_index == j]
        labels_ = labels[side_index == j]

        final_labels = labels_.copy()
        # reencode the labels to take into account the added clusters
        final_labels[labels_ == 2] = 4
        # select central cluster
        data_ = data_[labels_ == 1]

        g.fit(data_)
        w = g.weights_
        m = g.means_
        c = g.covariances_
        pred_labels = g.predict(data_)

        # directly sort the labels according to the precentral coordinates of the cluster
        t = np.argsort(m, axis=0)[:, 0]
        sorted_means = m[t]
        sorted_cov = c[t]
        sorted_weigth = w[t]
        sorted_pred_labels = pred_labels.copy()

        for z, s in enumerate(t):
            # s+1 to account for the existence of ventral cluster
            sorted_pred_labels[pred_labels == s] = z + 1
        final_labels[labels_ == 1] = sorted_pred_labels
        np.save(CLUSTERING_LABELS[side], final_labels)
