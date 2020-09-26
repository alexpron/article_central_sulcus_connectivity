import os
import numpy as np
import pandas as pd
from libs.tools.ppfm import get_hemisphere_group_pp
from libs.figures.connectivity_spaces import connectivity_profile

if __name__ == "__main__":

    from configuration.configuration import (
        SIDES,
        X_GRID,
        Y_GRID,
        PPFM_TABLES,
        U_FIBERS_GROUP_PROFILES,
        GROUP_DENSITIES_MAX,
        FIG_GROUP_PROFILES,
    )

    ppfm_df = pd.read_csv(PPFM_TABLES["final"])
    X = np.load(X_GRID)
    Y = np.load(Y_GRID)

    for j, side in enumerate(SIDES):
        if os.path.exists(U_FIBERS_GROUP_PROFILES[(side, "global_mean")]):
            ppfm = get_hemisphere_group_pp(
                ppfm_df, 100206, side
            )  # same coordinate across subjects, choose one
            density = np.load(U_FIBERS_GROUP_PROFILES[(side, "global_mean")])
            connectivity_profile(
                X,
                Y,
                density,
                path_fig=FIG_GROUP_PROFILES[side],
                title=None,
                vmin=0,
                vmax=GROUP_DENSITIES_MAX,
                colorbar=False,
                ppfm=ppfm,
                ppfm_label="Mean  PPFM ",
            )
        else:
            pass
