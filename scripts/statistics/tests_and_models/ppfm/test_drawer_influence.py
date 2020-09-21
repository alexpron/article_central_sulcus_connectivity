import pandas as pd
import seaborn as sns
import os
from matplotlib import pyplot as plt
from configuration import DIR_OUT
from scipy.stats import shapiro, mannwhitneyu, levene, ttest_1samp, ttest_ind, ttest_rel

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
    A = df.loc[df["Drawer"] == "Alex", "PP_CS_Coord_Iso"].values
    W_a, p_a = shapiro(A)
    O = df.loc[df["Drawer"] == "Olivier", "PP_CS_Coord_Iso"].values
    W_o, p_o = shapiro(O)

    print
    W, p
    print
    W_a, p_a
    print
    W_o, p_o

    W_v, p_v = levene(A, O)
    print
    W_v, p_v

    t, p_t = ttest_ind(A, O)
    print
    t, p_t

    # #
    # # sns.distplot(L,label='Left')
    # # sns.distplot(R,label='Right')
    # # plt.legend()
    # # plt.title('Distribution of Pli de Passage locations \n along the central sulcus fundus (ventral to dorsal)')
    # # plt.show()
    # t_d , p_td = ttest_ind(A, O)
    #            = mannwh
    # print t_d, p_td
    # print t_a, p_ta
