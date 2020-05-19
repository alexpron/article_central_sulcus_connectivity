import os
import numpy as np




if __name__ == '__main__':


    group_coordinates = np.zeros(U_fibers_extremities_index.shape)

    for p in PARAMS:
        for i, sub in enumerate(SUBJ_LIST):
            for j, side in enumerate(SIDES):
                        for k, g in enumerate(GYRI):

                            index = U_fibers_extremities_index[hemispheres_index == (len(SIDES) * i + j)][:,k]
                            path_param = os.path.join(DIR_OUT,'gyral_crests', sub + '_' + side + '_' + g + '_' +
                                                       p + '_' + 'param.npy')
                            param = np.load(path_param)
                            coordinates = param[index]
                            #small hack, for some unknown reason it is not possible to hash a selection
                            a = group_coordinates[hemispheres_index == (len(SIDES) * i + j)]
                            a[:, k] = coordinates
                            group_coordinates[hemispheres_index == (len(SIDES) * i + j)] = a
        np.save(os.path.join(DIR_OUT, 'connectivity','coordinates','raw',  'U_fibers_coord' + '_' + p + '.npy'),
                group_coordinates)





