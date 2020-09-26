import numpy as np
import pandas as pd
from libs.figures.connectivity_spaces import clusters_as_dots
from libs.tools.ppfm import get_hemisphere_subject_pp
from configuration.configuration import (
    PPFM_TABLES,
    U_FIBERS_COORD,
    HEMI_INDEXES_FILT,
    SIDES,
    CLUSTERING_LABELS,
    SUBJ_LIST,
    FIG_CLUSTERS_INDIV_SPACE,
)

if __name__ == "__main__":

    ppfm = pd.read_csv(PPFM_TABLES["final"])
    data = np.load(U_FIBERS_COORD["iso"])
    hemispheres_index = np.load(HEMI_INDEXES_FILT)
    side_index = np.mod(hemispheres_index, 2)

    for j, side in enumerate(SIDES.keys()):
        labels = np.load(CLUSTERING_LABELS[side])
        data_ = data[side_index == j]
        data_ = data_[labels != -1]
        labels_ = labels[labels != -1]
        hemi_index = hemispheres_index[side_index == j]
        hemi_index = hemi_index[labels != -1]

        for i, subject in enumerate(SUBJ_LIST):
            index = i * len(SIDES) + j
            data_sub = data_[hemi_index == index]
            labels_sub = labels_[hemi_index == index]

            title = None
            subject_pp = get_hemisphere_subject_pp(ppfm, subject, side)
            path_fig = FIG_CLUSTERS_INDIV_SPACE[(subject, side)]

            clusters_as_dots(
                data_sub,
                labels_sub,
                path_fig=path_fig,
                ppfm=subject_pp,
                ppfm_label="Individual PPFM",
                title=title
            )
