import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy.stats import levene, shapiro, ttest_1samp
from statsmodels.stats.anova import anova_lm
import seaborn as sns
import statsmodels.formula.api as smf
from variables import DIR_OUT

if __name__ == "__main__":

    path_df = os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_label_level.csv")
    df = pd.read_csv(path_df)
    labels = np.unique(df["Label"].values)
    # for l in labels:
    #     df_l = df.loc[df['Label']==l]
    #     L = df_l.loc[df_l['Hemisphere']=='L','Nb_Streamlines_Label'].values
    #     R = df_l.loc[df_l['Hemisphere'] == 'R', 'Nb_Streamlines_Label'].values
    #     A = 2.0*(R - L)/(R + L)
    #     W, p = shapiro(A) #All coefficient distributions are gaussian
    #     print "Label", l
    #     print "Normal Test", W, p
    #     t, p_t = ttest_1samp(A,0.0)
    #     print "Comp to 0", t, p_t
    for l in [0, 1, 2]:
        df_l = df.loc[df["Label"] == l]
        L = df_l.loc[df_l["Hemisphere"] == "L", "Nb_Streamlines_Label"].values
        R = df_l.loc[df_l["Hemisphere"] == "R", "Nb_Streamlines_Label"].values
        A = 2.0 * (R - L) / (R + L)
        new_df_l = df_l.drop_duplicates("Subject")
        new_df_l["Assymetry"] = A
        model = smf.ols("Assymetry ~ C(HandednessQ)*C(Gender)", data=new_df_l).fit()
        summary = model.summary()
        anova = anova_lm(model)
        # print summary
        print
        "Label ", l, "\n"
        print
        anova
        print
        "\n"
