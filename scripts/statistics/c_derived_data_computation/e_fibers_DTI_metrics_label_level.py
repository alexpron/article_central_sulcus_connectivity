import os
import numpy as np
import pandas as pd
from variables import DIR_IN, DIR_OUT, DIR_JAM

if __name__ == "__main__":
    path_df = os.path.join(DIR_IN, "label_tract_DTI_metrics.csv")
    path_hemi_df = os.path.join(DIR_OUT, "inter_tables", "hemispheres_level.csv")
    df = pd.read_csv(path_df)

    hemi_level = pd.read_csv(path_hemi_df)

    for name, group in df.groupby("Label"):
        print
        name, group
        group = group.reset_index(drop=True)
        fused_hemi_level = pd.merge(
            left=hemi_level, right=group, on=["Subject", "Hemisphere"]
        )
        fused_hemi_level.to_csv(
            os.path.join(
                DIR_JAM, "volume_streamlines_label_level" + str(name) + ".csv"
            ),
            index=False,
        )

        # transform the data into Repeated Measures (RM) format
        init_variables = [
            "Mesh_Area",
            "Fiedler_Length",
            "Roi_Area",
            "Max_Geo_Depth",
            "PP_CS_Depth",
            "FA",
            "MD",
            "RD",
        ]
        L_var = [v + "_L" for v in init_variables]
        R_var = [v + "_R" for v in init_variables]
        Ass_var = [v + "_" + "Asymmetry" for v in init_variables]
        L_dict = {v: L_var[i] for i, v in enumerate(init_variables)}
        R_dict = {v: R_var[i] for i, v in enumerate(init_variables)}

        hemispheres = fused_hemi_level.groupby("Hemisphere")

        L = hemispheres.get_group("L")
        R = hemispheres.get_group("R")

        L = L.rename(index=str, columns=L_dict)
        L = L.reset_index(drop=True)
        L = L.drop(columns=["Hemisphere"])

        R = R.rename(index=str, columns=R_dict)
        R = R.reset_index(drop=True)
        R = R.drop(columns=["Hemisphere"])
        # remove subject level variables to avoid doublons
        R = R.drop(
            columns=[
                "Gender",
                "Age_in_Yrs",
                "Handedness",
                "PMAT24_A_CR",
                "Dexterity_AgeAdj",
                "Strength_AgeAdj",
                "HandednessQ",
                "AgeQ",
                "PMAT24_A_CR_Q",
                "ICV",
            ]
        )

        final_df = pd.merge(left=L, right=R, on="Subject")

        # compute asymmetry coefficients
        for i in range(len(init_variables)):
            final_df[Ass_var[i]] = (
                2.0
                * (final_df[R_var[i]] - final_df[L_var[i]])
                / (final_df[R_var[i]] + final_df[L_var[i]])
            )

        path_df_out = os.path.join(
            DIR_JAM, "streamlines_DTI_metrics_label_level_" + str(name) + "RM.csv"
        )

        final_df.to_csv(path_df_out, index=False)
