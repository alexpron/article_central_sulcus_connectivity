import os
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from scipy.stats import shapiro
from variables import DIR_OUT, DIR_JAM
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(DIR_OUT, 'derived_tables', 'nb_streamlines_hemi_level.csv'))
    df['PP_CS_Depth_Normalised'] = df['PP_CS_Depth'] / df['Max_Geo_Depth']
    # df['Roi_Area_Normalised']
    # df.to_csv(os.path.join(DIR_OUT,'derived_tables','nb_streamlines_hemi_level_norm.csv'), index=False)
    # model = smf.ols('Nb_Streamlines_Hemi ~ PP_CS_Depth_Normalised + C(Hemisphere) + C(HandednessQ) + Roi_Area',data=df).fit()
    model = smf.ols('PP_CS_Depth_Normalised ~ C(Hemisphere)', data=df).fit()
    resid = model.resid
    W, p = shapiro(resid)
    print
    W, p
    summary = model.summary()
    print
    summary
    anova = anova_lm(model, type=3)
    print
    anova
