import os
import numpy as np
from soma import aims
from libs.connectivity_space import get_streamline_coord_on_gyri

if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, GYRI, MESHES, ASSO_TRACT_NEAREST_VERTEX, U_FIBERS_MASK, GYRAL_CRESTS, GEO_DISTS, U_FIBERS_INDEXES, HEMI_INDEXES

    pre_central_index = np.array([])
    post_central_index = np.array([])
    hemispheres_index = np.array([])

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES.keys()):
            if os.path.exists(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 's')]) and os.path.exists(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 'e')]):
                s = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 's')])
                e = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 'e')])
                mesh = aims.read(MESHES[(subject, side)])
                U_fibers = U_FIBERS_MASK[(subject, side)]
                #selecting the U fibers extremities
                U_s = s[U_fibers]
                U_e = e[U_fibers]
                # build an index at hemisphere level
                h_index = (len(SIDES) * i + j) * np.ones(len(U_s))
                hemispheres_index = np.concatenate((hemispheres_index, h_index))
                # computing the corresponding vertex on the gyral line
                pre = np.load(GYRAL_CRESTS[(subject, side, GYRI[0])])
                post = np.load(GYRAL_CRESTS[(subject, side, GYRI[1])])

                dist_to_pre = np.array(aims.read(GEO_DISTS[(subject, side, GYRI[0])])[0])
                dist_to_post = np.array(aims.read(GEO_DISTS[(subject, side, GYRI[1])])[0])

                pre_index, post_index = get_streamline_coord_on_gyri(U_s, U_e, pre, post, dist_to_pre,dist_to_post,mesh)
                pre_central_index = np.concatenate((pre_central_index,pre_index))
                post_central_index = np.concatenate((post_central_index, post_index))


    group_index = np.zeros((len(pre_central_index),2), dtype=int)
    group_index[:, 0] = pre_central_index
    group_index[:, 1] = post_central_index

    np.save(U_FIBERS_INDEXES, group_index)
    np.save(HEMI_INDEXES, hemispheres_index)














