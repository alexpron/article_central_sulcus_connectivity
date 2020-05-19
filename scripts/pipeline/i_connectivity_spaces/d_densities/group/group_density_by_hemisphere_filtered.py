import os
import numpy as np
from pipeline.h_connectivity_spaces.c_densities.densities import estimate_pseudo_density
from variables import DIR_OUT, SIDES


if __name__ == '__main__':
    #names of the initial densities
    DENSITIES = ['global_mean']
    radius = 10
    dir_connect = os.path.join(DIR_OUT, 'connectivity')
    dir_densities = os.path.join(dir_connect,'densities')
    path_X = os.path.join(dir_densities, 'X.npy')
    path_Y = os.path.join(dir_densities, 'Y.npy')
    path_hemispheres_index = os.path.join(dir_connect,'indexes','hemispheres_index_filtered.npy')

    hemispheres_index = np.load(path_hemispheres_index)
    #even --> L odd --> R
    sides_index = np.mod(hemispheres_index, 2)

    for i, d in enumerate(DENSITIES):
        path_coord = os.path.join(dir_connect, 'coordinates', 'length_filtered',
                                         'U_fibers_coord'+ '_' + d + '.npy')
        coord = np.load(path_coord)
        for j, side in enumerate(SIDES):
            #coherent name to be consistent between scripts
            filename = d + '_' + side + '_' + 'filtered' + '_' + 'radius' + '_' + str(radius)
            path_density = os.path.join(dir_densities, 'group',  filename + '.npy')

            new_coord = coord[sides_index == j]

            X, Y, Z = estimate_pseudo_density(new_coord,factor=radius)
            np.save(path_density, Z)
            if not os.path.exists(path_X) and not os.path.exists(path_Y):
                np.save(path_X, X)
                np.save(path_Y, Y)






