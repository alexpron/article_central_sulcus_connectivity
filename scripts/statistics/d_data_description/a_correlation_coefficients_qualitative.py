import os
import math
from scipy.stats import chi2_contingency
import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt
from variables import DIR_OUT, DIR_FIG


def cramersV(nrows, ncols, chisquared, correct_bias=False):
    nobs = nrows * ncols
    if correct_bias is True:
        phi = 0
    else:
        phi = chisquared / nobs
    V = np.sqrt((phi ** 2) / (min(nrows - 1, ncols - 1)))
    return V


def tshuprowsT(nrows, ncols, chisquared, correct_bias=True):
    nobs = nrows * ncols
    phi = chisquared / nobs
    T = np.sqrt((phi ** 2) / np.sqrt((nrows - 1) * (ncols - 1)))
    return T


if __name__ == '__main__':
    df = pd.read_csv(os.path.join(DIR_OUT, 'derived_tables', 'nb_streamlines_hemi_level.csv'))
    groups = ['Male', 'Female']
    quantitative_variables = ['Dexterity_AgeAdj', 'Strength_AgeAdj', 'Fiedler_Length', 'ICV', 'Mesh_Area',
                              'Max_Geo_Depth',
                              'PP_CS_Coord_Iso', 'PP_CS_Depth', 'Nb_Streamlines_Hemi']
    qualitative_variables = ['Gender', 'AgeQ', 'HandednessQ', 'PMAT24_A_CR_Q']

    quantitative = df[quantitative_variables]
    corr_matrix = np.corrcoef(quantitative, rowvar=False)
    mask = np.zeros_like(corr_matrix)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr_matrix, mask=mask, annot=True, center=0, square=True, linewidths=0.5, vmin=-1, vmax=1,
                cmap='Spectral_r', xticklabels=quantitative_variables, yticklabels=quantitative_variables)
