import os
import numpy as np
import pandas as pd
from libs.figures.connectivity_spaces import (
    get_hemisphere_group_pp,
    get_hemisphere_subject_pp,
    connectivity_profile,
)

if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        X_GRID,
        Y_GRID,
        PPFM_TABLES,
        PARAMETRISATIONS,
        U_FIBERS_INDIV_PROFILES,
        FIG_INDIV_PROFILES,
    )

    X = np.load(X_GRID)
    Y = np.load(Y_GRID)
    maxi = []
    ppfm_df = pd.read_csv(PPFM_TABLES["final"])
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            subject_pp = get_hemisphere_subject_pp(ppfm_df, subject, side)
            group_pp = get_hemisphere_group_pp(ppfm_df, subject, side)
            for k, param in enumerate(PARAMETRISATIONS[:2]):
                if os.path.exists(U_FIBERS_INDIV_PROFILES[(subject, side, param)]):
                    density = np.load(U_FIBERS_INDIV_PROFILES[(subject, side, param)])
                    maxi.append(density.max())
                    if param == "iso":
                        ppfm = subject_pp
                        ppfm_label = "Individual PPFM"
                        ppfm_tag = "individual"
                    else:
                        ppfm = group_pp
                        ppfm_label = "Mean PPFM"
                        ppfm_tag = "group"
                    connectivity_profile(
                        X,
                        Y,
                        density,
                        path_fig=FIG_INDIV_PROFILES[(subject, side, param, ppfm_tag)],
                        title=None,
                        nb_levels=150,
                        vmin=None,
                        vmax=None,
                        colorbar=False,
                        colorbar_tiks_step=500,
                        ppfm=ppfm,
                        ppfm_label=ppfm_label,
                    )
                else:
                    pass
