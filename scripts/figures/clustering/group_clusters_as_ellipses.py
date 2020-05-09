import numpy as np
import os
from variables import DIR_OUT, DIR_FIG, SIDES
from pipeline.m_visualisation.visualisation import density_and_clusters_ellipses

def compute_params(data, labels):
    label_values = np.unique(labels)
    means = [np.mean(data[labels==l],axis=0)for l in label_values]
    cov = [np.cov(data[labels==l],rowvar=False)for l in label_values]
    return means, cov




if __name__ == '__main__':

    d = 'global_mean'
    path_data = os.path.join(DIR_OUT, 'connectivity','coordinates','length_filtered','U_fibers_coord_global_mean.npy')
    path_hemispheres_index = os.path.join(DIR_OUT,'connectivity','indexes','hemispheres_index_filtered.npy')

    X = np.load(os.path.join(DIR_OUT,'connectivity','densities','X.npy'))
    Y = np.load(os.path.join(DIR_OUT,'connectivity','densities','Y.npy'))


    data = np.load(path_data)
    hemisphere_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemisphere_index, 2)


    #clustering by hemisphere
    for j, side in enumerate(SIDES):
        data_ = data[side_index == j]
        path_labels = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed', 'global_mean_all_labels_' + side + '.npy')
        labels_ = np.load(path_labels)

        path_density = os.path.join(DIR_OUT,'connectivity','densities','group','global_mean_' + side + '_filtered_radius_5.npy')
        density = np.load(path_density)

        #path_fig = os.path.join(DIR_FIG,'connectivity_space', 'group_clustering', d + '_' + side  +'.eps' )
        #display_data = data_
        #display_labels = labels_
        display_data = data_[labels_ != -1]
        display_labels = labels_[labels_ != -1]
        means, cov = compute_params(display_data, display_labels)
        path_fig = os.path.join(DIR_FIG,'connectivity_space','group_clustering','global_mean_' + side + '_clusters_as_ellipses.tiff')
        density_and_clusters_ellipses(X,Y, density,means,cov,vmin=0,vmax=8000,path_fig=path_fig)























