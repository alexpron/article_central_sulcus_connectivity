import os
import numpy as np
from libs.connectivity_space import estimate_pseudo_density

if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, PARAMETRISATIONS, HEMI_INDEXES, U_FIBERS_COORD, \
        DENSITIES_RADIUS, U_FIBERS_INDIV_PROFILES, X_GRID, Y_GRID

    hemispheres_index = np.load(HEMI_INDEXES)

    for i, param in enumerate(PARAMETRISATIONS):

        coord = np.load(U_FIBERS_COORD)
        for j, subject in enumerate(SUBJ_LIST):
            for k, side in enumerate(SIDES):
                index = j * len(SIDES) + k
                new_coord = coord[hemispheres_index == index]
                X, Y, Z = estimate_pseudo_density(new_coord, factor=DENSITIES_RADIUS)
                np.save(U_FIBERS_INDIV_PROFILES[(subject, side, param)], Z)
                if not os.path.exists(X_GRID) and not os.path.exists(Y_GRID):
                    np.save(X_GRID, X)
                    np.save(Y_GRID, Y)
