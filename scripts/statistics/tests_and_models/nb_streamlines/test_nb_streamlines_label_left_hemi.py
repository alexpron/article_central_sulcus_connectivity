import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy.stats import levene, shapiro, ttest_1samp, kruskal, mannwhitneyu
from statsmodels.stats.anova import anova_lm
import seaborn as sns
import statsmodels.formula.api as smf
from variables import DIR_OUT

if __name__ == "__main__":
    path_df = os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_label_level.csv")
    df = pd.read_csv(path_df)
    new_df = df.loc[(df["Hemisphere"] == "L") & (df["Label"] != -1)]
    labels = np.unique(df["Label"].values)
    sns.lmplot(x="PP_CS_Coord_Iso", y="Nb_Streamlines_Label", hue="Label", data=new_df)
    plt.show()
    # for l in labels:
    # #    nb_stream = new_df.loc[new_df['Label']==l,'Nb_Streamlines_Label'].values
    # #     W, p = shapiro(nb_stream)
    # #     print "Label", l,  W,p
    # #     sns.distplot(nb_stream,hist=False,label='Cluster ' + str(l))
    # # plt.title('Streamlines number distribution, Contralateral Hemisphere')
    # # plt.show()
    #     M = new_df.loc[(new_df['Label']==l) & (new_df['Gender']=='M'),'Nb_Streamlines_Label'].values
    #     F = new_df.loc[(new_df['Label'] == l) & (new_df['Gender'] == 'F'), 'Nb_Streamlines_Label'].values
    #     H = new_df.loc[(new_df['Label'] == l) & (new_df['HandednessQ'] == 'High'), 'Nb_Streamlines_Label'].values
    #     L = new_df.loc[(new_df['Label'] == l) & (new_df['HandednessQ'] == 'Low'), 'Nb_Streamlines_Label'].values
    #     #W, p = kruskal(H, L)
    #     #print "Label", l,  W, p
    #     W, p = mannwhitneyu(L, H)
    #     #W, p = kruskal(H, L)
    #     print "Label",l,  W, p
