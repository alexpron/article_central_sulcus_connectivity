"""

"""
import os
import numpy as np
from libs.connectivity_space import estimate_pseudo_density

if __name__ == "__main__":

    from configuration.configuration import (
        HEMI_INDEXES,
        SIDES,
        PARAMETRISATIONS,
        DENSITIES_RADIUS,
        U_FIBERS_COORD,
        U_FIBERS_GROUP_PROFILES,
        X_GRID,
        Y_GRID,
    )

    hemispheres_index = np.load(HEMI_INDEXES)
    sides_index = np.mod(hemispheres_index, 2)

    for i, param in enumerate(PARAMETRISATIONS):
        coord = np.load(U_FIBERS_COORD[param])
        for j, side in enumerate(SIDES.keys()):
            new_coord = coord[sides_index == j]
            X, Y, Z = estimate_pseudo_density(new_coord, factor=DENSITIES_RADIUS)
            np.save(U_FIBERS_COORD[(side, param)], Z)
            if not os.path.exists(X_GRID) and not os.path.exists(Y_GRID):
                np.save(X_GRID, X)
                np.save(Y_GRID, Y)
