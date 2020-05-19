import numpy as np
from libs.clustering import dbscan_density_clustering

if __name__ == '__main__':

    from configuration.configuration import SIDES, U_FIBERS_COORD, HEMI_INDEXES, DBSCAN_LABELS

    data = np.load(U_FIBERS_COORD['global_mean'])
    hemisphere_index = np.load(HEMI_INDEXES)
    side_index = np.mod(hemisphere_index, 2)
    global_labels = np.zeros_like(hemisphere_index)

    for j, side in enumerate(SIDES):
        data_ = data[side_index == j]
        labels = dbscan_density_clustering(data_)
        global_labels[side_index == j] = labels
    np.save(DBSCAN_LABELS, global_labels)
