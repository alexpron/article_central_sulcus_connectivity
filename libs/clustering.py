import numpy as np
from sklearn.cluster import DBSCAN
from configuration.configuration import EPS, NORM_THRESHOLD



def estimate_weights(coordinates):
    unique_coords, inverse, weigth = np.unique(coordinates,return_inverse=True,return_counts=True,axis=0)
    return unique_coords, inverse, weigth

def dbscan_density_clustering(data, eps=EPS, normalised_threshold=NORM_THRESHOLD):
    unique_data, inverse, weigth = estimate_weights(data)
    total_weigth = np.sum(weigth)
    #normalisation to work with densities
    min_sample = total_weigth*normalised_threshold
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