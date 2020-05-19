"""
U-fibers of a sulcus are selected as streamlines whose terminations are located into both adjacent gyri areas
"""

from soma import aims
import numpy as np

if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, GYRI, ASSO_TRACT_NEAREST_VERTEX, ADJACENT_GYRI_ROI, \
        U_FIBERS_MASK

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES.keys()):
            pre_roi = np.array(aims.read(ADJACENT_GYRI_ROI[(subject, side, GYRI[0])])[0])
            post_roi = np.array(aims.read(ADJACENT_GYRI_ROI[(subject, side, GYRI[1])])[0])
            e = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 'e')])
            s = np.load(ASSO_TRACT_NEAREST_VERTEX[(subject, side, 's')])
            U_fibers = (pre_roi[e] != 0) * (post_roi[s] != 0)
            np.save(U_FIBERS_MASK[(subject, side)], U_fibers)
