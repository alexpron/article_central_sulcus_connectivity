import os
import pandas as pd
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import plot_partregress
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import normaltest, ttest_rel, wilcoxon, ranksums, levene, ttest_ind
from variables import DIR_OUT

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(DIR_OUT, "inter_tables", "hemispheres_level.csv"))
    # subgroups = df.groupby(['Gender'])
    # mesh_areas = [group['Mesh_Area'].values for name, group in subgroups]
    # W, p = levene(mesh_areas[0],mesh_areas[1])
    # print W, p
    #
    # model = ols('Mesh_Area ~ C(Hemisphere)*C(AgeQ)',data=df).fit()
    # summary = model.summary()
    # print summary
    # anova = sm.stats.anova_lm(model)
    sns.jointplot(x="Mesh_Area", y="ICV", data=df, kind="reg")
    plt.show()

    # model = ols('ICV ~ np.power(Mesh_Area,1.5)-1', data=df).fit()
    # summary = model.summary()
    # print summary
    # # anova = sm.stats.anova_lm(model)
    # # print anova
