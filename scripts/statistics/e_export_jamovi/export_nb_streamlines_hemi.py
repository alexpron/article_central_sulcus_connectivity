import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == "__main__":
    df = pd.read_csv(
        os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_hemi_level.csv")
    )
    df.to_csv(os.path.join(DIR_JAM, "nb_streamlines_hemi_level.csv"), index=False)
