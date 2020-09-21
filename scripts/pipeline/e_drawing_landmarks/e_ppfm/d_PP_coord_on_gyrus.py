"""
Retrieve the coordinate of the PPFM along the crest lines according to the chosen parametrisation
"""

import numpy as np
import pandas as pd
from configuration.configuration import (
    SUBJ_LIST,
    SIDES,
    GYRI,
    PPFM_TABLES,
    GYRAL_PARAMETRISATIONS,
)

if __name__ == "__main__":

    df = pd.read_csv(PPFM_TABLES["gyri_index"])
    df["PP_Pre_Coord_Iso"] = -1
    df["PP_Post_Coord_Iso"] = -1
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for k, gyrus in enumerate(GYRI):
                gyr_suffix = gyrus.replace("central", "")
                gyr_suffix = gyr_suffix.upper()[0] + gyr_suffix[1:]
                variable_in = "PP" + "_" + gyr_suffix + "_" + "Index_Line"
                variable_out = "PP" + "_" + gyr_suffix + "_" + "Coord_Iso"
                pp_index_gyrus = int(
                    df.loc[
                        (df["Subject"] == int(subject)) & (df["Hemisphere"] == side),
                        variable_in,
                    ]
                )
                gyrus_param = np.load(
                    GYRAL_PARAMETRISATIONS[
                        (subject, side, gyrus, "cleaned", "array", "iso")
                    ]
                )
                pp_coord = gyrus_param[pp_index_gyrus]
                df.loc[
                    (df["Subject"] == int(subject)) & (df["Hemisphere"] == side),
                    variable_out,
                ] = pp_coord
    df.to_csv(PPFM_TABLES["gyri_coord"])
