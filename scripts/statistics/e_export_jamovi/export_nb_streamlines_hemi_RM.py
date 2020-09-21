import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == "__main__":

    df = pd.read_csv(
        os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_hemi_level.csv")
    )

    variables = [
        "Mesh_Area",
        "Fiedler_Length",
        "Roi_Area",
        "Max_Geo_Depth",
        "PP_CS_Coord_Iso",
        "PP_Pre_Coord_Iso",
        "PP_Post_Coord_Iso",
        "PP_CS_Depth",
        "Nb_Streamlines_Hemi",
    ]

    subgroups = df.groupby("Hemisphere")
    L = subgroups.get_group("L")
    R = subgroups.get_group("R")
    L_var = [v + "_" + "L" for v in variables]
    R_var = [v + "_" + "R" for v in variables]
    A_var = [v + "_" + "Assymetry" for v in variables]
    L_dic = {v: L_var[i] for i, v in enumerate(variables)}
    R_dic = {v: R_var[i] for i, v in enumerate(variables)}
    L = L.rename(index=str, columns=L_dic)
    R = R.rename(index=str, columns=R_dic)
    R = R[["Subject"] + R_var]

    final = pd.merge(L, R, on="Subject")
    # print final.shape
    final = final.drop(columns="Hemisphere")
    for i, v in enumerate(variables):
        L = final[L_var[i]].values
        R = final[R_var[i]].values
        A = 2.0 * (R - L) / (R + L)
        final[A_var[i]] = A
    final.to_csv(os.path.join(DIR_JAM, "nb_streamlines_hemi_level_RM.csv"), index=False)
