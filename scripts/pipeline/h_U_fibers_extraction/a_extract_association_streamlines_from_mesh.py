import numpy as np
from soma import aims, aimsalgo



if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        MESHES,
        TRACTOGRAMS,
        NEAREST_VERTEX,
        NEAREST_VERTEX_N,
        ASSOCIATION_TRACTS
    )

    for i, subject in enumerate(SUBJ_LIST):
            l_mesh = aims.read(MESHES[subject, 'L', 'white'])
            l_s = len(np.array(l_mesh.vertex()))
            r_mesh = aims.read(MESHES[subject, 'R', "white"])
            r_s = len(np.array(r_mesh.vertex()))
            print(l_s, r_s)
            hemi_index = np.zeros(l_s + r_s)
            hemi_index[l_s:] = 1

            s_nearest = np.load(NEAREST_VERTEX[subject, 's'])
            e_nearest = np.load(NEAREST_VERTEX[subject, 'e'])

            hemi_s = hemi_index[s_nearest]
            hemi_e = hemi_index[e_nearest]

            tractogram = np.load(TRACTOGRAMS[subject])

            for j, side in enumerate(SIDES.keys()):
                association_tracts_filter = (hemi_s == hemi_e) * (hemi_s == j)
                association_tracts = tractogram[association_tracts_filter == True]
                np.save(ASSOCIATION_TRACTS[subject, side], association_tracts)
                s_nearest_hemi = s_nearest[association_tracts_filter == True]
                e_nearest_hemi = e_nearest[association_tracts_filter == True]
                if j == 1:
                    s_nearest_hemi -= l_s
                    e_nearest_hemi -= l_s
                np.save(NEAREST_VERTEX_N(subject, side, 's'), s_nearest_hemi)
                np.save(NEAREST_VERTEX_N(subject, side, 'e'), e_nearest_hemi)









