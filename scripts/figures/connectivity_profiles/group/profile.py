import os
import numpy as np
import pandas as pd
from libs.figures.connectivity_spaces import density_plot_group, get_hemisphere_group_pp

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
                ppfm_df, "102006", side
            )  # same coordinate across subjects, choose one
            density = np.load(U_FIBERS_GROUP_PROFILES[(side, "global_mean")])
            density_plot_group(
                X,
                Y,
                density,
                pli_passage=ppfm,
                path_fig=FIG_GROUP_PROFILES[side],
                title=None,
                vmin=0,
                vmax=GROUP_DENSITIES_MAX,
            )
        else:
            pass
