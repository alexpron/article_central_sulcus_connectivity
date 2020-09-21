import pandas as pd
import seaborn as sns
import os
from matplotlib import pyplot as plt
from configuration import DIR_OUT
from scipy.stats import (
    shapiro,
    mannwhitneyu,
    levene,
    ttest_1samp,
    ttest_ind,
    ttest_rel,
    kruskal,
)

if __name__ == "__main__":
    df = pd.read_csv(
        os.path.join(DIR_OUT, "ppfm", "tables", "pp_manual_drawing_coord_sulcus.csv")
    )
    df = df[["Subject", "Hemisphere", "PP_CS_Coord_Iso", "Drawer"]]
    df = df.dropna()
    # Test normality of the different distributions
    # Whole distribution
    W, p = shapiro(df["PP_CS_Coord_Iso"].values)
    # Left Distribution
    L_O = df.loc[
        (df["Hemisphere"] == "L") & df["Drawer"] == "Olivier", "PP_CS_Coord_Iso"
    ].values
    R_O = df.loc[
        (df["Hemisphere"] == "R") & df["Drawer"] == "Olivier", "PP_CS_Coord_Iso"
    ].values
    L_A = df.loc[
        (df["Hemisphere"] == "L") & df["Drawer"] == "Alex", "PP_CS_Coord_Iso"
    ].values
    R_A = df.loc[
        (df["Hemisphere"] == "R") & df["Drawer"] == "Alex", "PP_CS_Coord_Iso"
    ].values

    W, p = kruskal(L_O, R_O, L_A, R_A)
