import os
import numpy as np
from pipeline.h_connectivity_spaces.c_densities.densities import estimate_pseudo_density
from variables import DIR_OUT, SUBJ_LIST, SIDES


if __name__ == '__main__':
    #ds of the initial densities
    DENSITIES = ['iso', 'global_mean', 'mean_by_hemi']
    RADIUS = [1, 3, 5, 10]
    TYPE = ['raw','filtered']
    path_X = os.path.join(DIR_OUT, 'connectivity', 'densities', 'X.npy')
    path_Y = os.path.join(DIR_OUT, 'connectivity', 'densities', 'Y.npy')
    path_hemispheres_index = os.path.join(DIR_OUT,'connectivity','indexes','hemispheres_index_filtered.npy')
    #loading values
    hemispheres_index = np.load(path_hemispheres_index)

    for i, d in enumerate(DENSITIES):
        path_coord = os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'length_filtered',
                                         'U_fibers_coord' + '_' + d + '.npy')
        coord = np.load(path_coord)
        for j,subject in enumerate(SUBJ_LIST):
            for k, side in enumerate(SIDES):
                index = j*len(SIDES) + k
                new_coord = coord[hemispheres_index == index]
                for radius in RADIUS:
                    filename = d + '_' + subject + '_' + side + '_' + 'filtered' + '_' + 'radius' + '_' + str(radius)
                    path_density = os.path.join(DIR_OUT, 'connectivity', 'densities', 'subjects', filename + '.npy')
                    X, Y, Z = estimate_pseudo_density(new_coord,factor=radius)
                    np.save(path_density, Z)
                    if not os.path.exists(path_X) and not os.path.exists(path_Y):
                        np.save(path_X, X)
                        np.save(path_Y, Y)






