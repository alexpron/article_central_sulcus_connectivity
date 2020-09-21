import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == "__main__":

    path_df = os.path.join(DIR_OUT, "derived_tables", "centroids_iso.csv")
    df = pd.read_csv(path_df)
    for label, subdf in df.groupby("Label"):
        subdf.to_csv(
            os.path.join(DIR_JAM, "centroids" + "_" + str(label) + ".csv"), index=False
        )
