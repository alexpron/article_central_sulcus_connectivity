"""
U-fibers of a sulcus are selected as streamlines whose terminations are located into both adjacent gyri areas
"""

from soma import aims
import numpy as np

if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        GYRI,
        ASSO_TRACT_NEAREST_VERTEX,
        ADJ_GYRI_ROI,
        U_FIBERS_MASK,
    )

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES.keys()):
            print(subject, side)
            pre_roi = np.array(
                aims.read(ADJ_GYRI_ROI[(subject, side, GYRI[0])])
            )[0]
            post_roi = np.array(
                aims.read(ADJ_GYRI_ROI[(subject, side, GYRI[1])])
            )[0]
            print(pre_roi.shape)
            print(post_roi.shape)
            e = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, "e")])
            s = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, "s")])
            print(e.shape)
            print(s.shape)
            U_fibers = ((pre_roi[e] != 0) * (post_roi[s] != 0)) + (pre_roi[s] != 0)*(post_roi[e] != 0)
            np.save(U_FIBERS_MASK[(subject, side)], U_fibers)
