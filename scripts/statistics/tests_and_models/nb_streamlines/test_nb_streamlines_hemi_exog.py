import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from matplotlib import pyplot as plt
from scipy.stats import levene
from statsmodels.stats.anova import anova_lm
import seaborn as sns
import statsmodels.formula.api as smf
from variables import DIR_OUT

if __name__ == "__main__":
    path_df = os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_hemi_level.csv")
    df = pd.read_csv(path_df)
    # sns.lmplot(x='Mesh_Area',y='Nb_Streamlines_Hemi', hue='Hemisphere',data=df, truncate=True,robust=True)

    #
    model = smf.wls("Nb_Streamlines_Hemi ~ Mesh_Area -1", data=df).fit()
    print
    model.summary()
    df["Corrected_Nb_Streamlines_Hemi"] = model.resid
    #  plt.scatter(df['Mesh_Area'].values,df['Nb_Streamlines_Hemi'])
    #  plt.plot(df['Mesh_Area'].values, float(model.params)*(df['Mesh_Area'].values))
    #
    #  plt.show()
    #
    #  # model = smf.ols('Corrected_Nb_Streamlines_Hemi~ PP_CS_Coord_Iso', data=df).fit()
    #  # print model.summary()
    #  # anova = anova_lm(model)
    #  # print summary
    # # print anova
    #  model = smf.ols('Corrected_Nb_Streamlines_Hemi ~ C(Hemisphere)*C(HandednessQ)*C(Gender)*C(AgeQ)',data=df).fit()
    #  print model.summary()
    #  anova = anova_lm(model)
    #  print anova
    sns.catplot(
        x="Hemisphere",
        y="Corrected_Nb_Streamlines_Hemi",
        hue="HandednessQ",
        data=df,
        kind="box",
    )
    plt.show()
