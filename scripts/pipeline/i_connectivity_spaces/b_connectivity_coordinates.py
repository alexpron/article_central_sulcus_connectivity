import os
import numpy as np

if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, GYRI, PARAMETRISATIONS, GYRAL_PARAMETRISATIONS, \
        HEMI_INDEXES, U_FIBERS_INDEXES, U_FIBERS_COORD

    U_fibers_extremities_index = np.load(U_FIBERS_INDEXES)
    hemispheres_index = np.load(HEMI_INDEXES)
    group_coordinates = np.zeros(U_fibers_extremities_index.shape)

    for param in PARAMETRISATIONS:
        for i, subject in enumerate(SUBJ_LIST):
            for j, side in enumerate(SIDES.keys()):
                for k, gyrus in enumerate(GYRI):
                    index = U_fibers_extremities_index[hemispheres_index == (len(SIDES) * i + j)][:, k]
                    parametrisation = np.load(GYRAL_PARAMETRISATIONS[(subject, side, gyrus, 'cleaned', 'array', param)])
                    coordinates = param[index]
                    # small hack, for some unknown reason it is not possible to hash a selection
                    a = group_coordinates[hemispheres_index == (len(SIDES) * i + j)]
                    a[:, k] = coordinates
                    group_coordinates[hemispheres_index == (len(SIDES) * i + j)] = a
        np.save(U_FIBERS_COORD[param], group_coordinates)
