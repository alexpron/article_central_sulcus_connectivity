import numpy as np
import numpy as np
import os
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt
from variables import DIR_OUT, DIR_DATA, SUBJ_LIST, SIDES
import pandas as pd




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
        nn = NearestNeighbors(n_neighbors=100).fit(data)
        dist, ind = nn.kneighbors(data)
        d = np.sort(dist[:,-1])
        d = d[::-1]
        #np.save(os.path.join('/home/alex/PycharmProjects/HCP/central_sulcus_connectivity/data/output/group_clustering/dbscan_fixed/eps_param',side + '.npy'), dist)
        plt.plot(d.flatten())
        plt.yticks(np.arange(0,5,0.1))
        plt.show()
















