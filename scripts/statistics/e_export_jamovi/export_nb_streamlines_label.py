import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == "__main__":

    df = pd.read_csv(
        os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_label_level.csv")
    )
    df = df.loc[df["Label"] != -1]
    print
    df.columns
    df["PP_CS_Depth_Normalised"] = df["PP_CS_Depth"] / df["Max_Geo_Depth"]
    df["Streammlines_Density_Label"] = df["Nb_Streamlines_Label"] / df["Roi_Area"]
    df.to_csv(
        os.path.join(DIR_JAM, "inter", "nb_streamlines_label_level.csv"), index=False
    )

    for label, subdf in df.groupby("Label"):
        subdf.to_csv(
            os.path.join(
                DIR_JAM, "inter", "nb_streamlines_label_level_" + str(label) + ".csv"
            ),
            index=False,
        )
