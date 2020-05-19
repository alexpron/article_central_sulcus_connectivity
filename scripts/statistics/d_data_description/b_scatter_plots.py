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
    plt.show()

    #
    #
    # figure, axes = plt.subplots(ncols=2)
    # #
    # # for i, g in enumerate(groups):
    # #     df_g = df.loc[df['Gender'] == g[0]]
    # #     quantitative = df_g[['Dexterity_AgeAdj', 'Strength_AgeAdj', 'Fiedler_Length', 'ICV', 'Mesh_Area', 'Max_Geo_Depth',
    # #                        'PP_CS_Coord_Iso', 'PP_CS_Depth','Nb_Streamlines_Hemi']]
    # #     corr_matrix = np.corrcoef(quantitative,rowvar=False)
    # #     mask = np.zeros_like(corr_matrix)
    # #     mask[np.triu_indices_from(mask)] = True
    # #     sns.heatmap(corr_matrix,mask=mask,annot=True,center=0,square=True,linewidths=0.5,vmin=-1, vmax=1,cmap='Spectral_r',xticklabels=quatitative_variables,yticklabels=quatitative_variables,ax=axes[i])
    # #     axes[i].set_title(g)
    # # plt.show()
    #
    #
    # chi2_mat = np.zeros((len(qualitative_variables),len(qualitative_variables)))
    # T_mat =  np.zeros_like(chi2_mat)
    # CrV_mat = np.zeros_like(T_mat)
    # mask = np.zeros_like(chi2_mat)
    # mask[np.triu_indices_from(mask)] = True
    #
    # for i,q in enumerate(qualitative_variables):
    #     for j, k in enumerate(qualitative_variables):
    #
    #             tab = pd.crosstab(df[q],df[k])
    #             nrows, ncols = tab.shape
    #             chi2 = chi2_contingency(tab.values)
    #             chi2_mat[i,j] = chi2[0]
    #             T_mat[i,j] = tshuprowsT(nrows, ncols,chi2[0])
    #             CrV_mat[i, j] = cramersV(nrows, ncols,chi2[0])
    #
    # sns.heatmap(T_mat, mask=mask, annot=True, square=True, linewidths=0.5, vmin=0, vmax=1,
    #             cmap='Spectral_r', xticklabels=qualitative_variables, yticklabels=qualitative_variables, ax=axes[0])
    # sns.heatmap(CrV_mat, mask=mask, annot=True, square=True, linewidths=0.5, vmin=0, vmax=1,
    #             cmap='Spectral_r', xticklabels=qualitative_variables, yticklabels=qualitative_variables, ax=axes[1])
    # axes[0].set_title('Tschuprow Coefficient Matrix')
    # axes[1].set_title('Cramers Coefficient Matrix')
    # plt.show()

    #
    #
    #
    #     #sm.graphics.plot_corr(corr_matrix,xnames=['Dexterity_AgeAdj','Strength_AgeAdj','Fiedler_Length','ICV','Mesh_Area','Max_Geo_Depth','PP_CS_Coord_Iso','PP_CS_Depth','Nb_Streamlines_Hemi'])
    #     variables = ['Dexterity_AgeAdj', 'Strength_AgeAdj', 'Fiedler_Length', 'ICV', 'Mesh_Area', 'Max_Geo_Depth',
    #                        'PP_CS_Coord_Iso', 'PP_CS_Depth','Nb_Streamlines_Hemi']
    #     for i, v1 in enumerate(variables):
    #         for j, v2 in enumerate(variables):
    #             if i>j:
    #                 index = str(i + j)
    #                 figure, ax = plt.subplots()
    #                 ax = sns.scatterplot(v1,v2,hue='Hemisphere',data=df_g,ax=ax)
    #                 ax.set_title('Scatter Plot of quantitative variables ' + g  + ' Subgroup')
    #                 figure.savefig(os.path.join(DIR_FIG, g + '_' + index + '.png' ))
    #                 plt.close(figure)
    ###
    #     #qualitative variables
    # qualitative_variables = ['AgeQ','HandednessQ','PMAT24_A_CR_Q']
    # quantitative_variables = ['Dexterity_AgeAdj', 'Strength_AgeAdj', 'Fiedler_Length', 'ICV', 'Mesh_Area', 'Max_Geo_Depth',
    #                         'PP_CS_Coord_Iso', 'PP_CS_Depth','Nb_Streamlines_Hemi']
    # for i, q in enumerate(qualitative_variables):
    #     for j, k in enumerate(quantitative_variables):
    #
    #         axes = sns.catplot(x='Hemisphere',y=k, hue='Gender',kind='box',col=q,data=df)
    #         axes.savefig(os.path.join(DIR_FIG, q + '_' + k +  'v2.png'))
    #         plt.show()
    #         #figure.savefig(os.path.join(DIR_FIG, q + '_' + k +  'v2.png'))
    #
