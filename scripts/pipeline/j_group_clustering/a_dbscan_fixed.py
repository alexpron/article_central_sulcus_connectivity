import numpy as np
import numpy as np
import os
from sklearn.cluster import DBSCAN
from variables import DIR_OUT, DIR_DATA, SUBJ_LIST, SIDES
import pandas as pd

#declare constant fixed for this study
EPS = 3
ABS = 2300
NORM_THRESHOLD = ABS/249897.0

def estimate_weights(coordinates):
    unique_coords, inverse, weigth = np.unique(coordinates,return_inverse=True,return_counts=True,axis=0)
    return unique_coords, inverse, weigth

def dbscan_density_clustering(data,eps,normalised_threshold=NORM_THRESHOLD):
    unique_data, inverse, weigth = estimate_weights(data)
    total_weigth = np.sum(weigth)
    #normalisation to work with densities
    min_sample = total_weigth*normalised_threshold
    print min_sample
    db = DBSCAN(eps=eps, min_samples=min_sample).fit(X=unique_data, sample_weight=weigth)
    unique_labels = db.labels_
    labels = unique_labels[inverse]
    return labels

def random_dbscan_clustering(data, percentage=1.0,eps=EPS, normalised_threshold=NORM_THRESHOLD):
    n = data.shape[0]
    n_sample = int(n * percentage)
    np.random.shuffle(data)
    sample_data = data[:n_sample]
    rejected_data = data[n_sample:]
    labels = dbscan_density_clustering(sample_data,eps,normalised_threshold)
    return sample_data, labels, rejected_data


if __name__ == '__main__':

    d = 'global_mean'

    path_data = os.path.join(DIR_OUT, 'connectivity','coordinates','length_filtered','U_fibers_coord' + '_' + d +
                             '.npy')
    path_hemispheres_index = os.path.join(DIR_OUT,'connectivity','indexes','hemispheres_index_filtered.npy')
    dir_output = os.path.join(DIR_OUT, 'group_clustering','dbscan_fixed')


    data = np.load(path_data)
    hemisphere_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemisphere_index, 2)
    global_labels = np.zeros_like(hemisphere_index)
    print hemisphere_index.shape
    print global_labels.shape

    #clustering by hemisphere
    for j, side in enumerate(SIDES):
        data_ = data[side_index == j]
        print data_.shape
        labels = dbscan_density_clustering(data_, eps=EPS)
        global_labels[side_index == j] = labels
    path_labels = os.path.join(dir_output, d + '_' + 'labels' + '.npy')
    #print path_labels
    np.save(path_labels, global_labels)

















