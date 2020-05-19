import os

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from variables import DIR_OUT, DIR_FIG



if __name__ == '__main__':

    df = pd.read_csv(os.path.join(DIR_OUT,'derived_tables','nb_streamlines_hemi_level.csv'))
    quantitative_variables = ['Dexterity_AgeAdj', 'Strength_AgeAdj', 'Fiedler_Length', 'ICV', 'Mesh_Area', 'Max_Geo_Depth',
                            'PP_CS_Coord_Iso', 'PP_CS_Depth','Nb_Streamlines_Hemi']
    qualitative_variables = ['Gender','Hemisphere']

    figure, axes =plt.subplots(nrows=2,ncols=2)

    subgroups = df.groupby(qualitative_variables)
    for i, groups in enumerate(subgroups):

        quantitative = groups[1][quantitative_variables]
        corr_matrix = np.corrcoef(quantitative,rowvar=False)
        mask = np.zeros_like(corr_matrix)
        mask[np.triu_indices_from(mask)] = True

        if groups[0][0] == 'F' and groups[0][1] == 'L' :
            sns.heatmap(corr_matrix, mask=mask, annot=True, center=0, square=True, linewidths=0.5, vmin=-1, vmax=1,
                        cmap='Spectral_r', yticklabels=quantitative_variables,ax=axes[0,0])

        elif groups[0][0] == 'F' and groups[0][1] == 'R':
            sns.heatmap(corr_matrix, mask=mask, annot=True, center=0, square=True, linewidths=0.5, vmin=-1, vmax=1,
                        cmap='Spectral_r', ax=axes[0, 1])

        if groups[0][0] == 'M' and groups[0][1] == 'L':
            sns.heatmap(corr_matrix, mask=mask, annot=True, center=0, square=True, linewidths=0.5, vmin=-1, vmax=1,
                        cmap='Spectral_r', xticklabels=quantitative_variables, yticklabels=quantitative_variables, ax=axes[1, 0])

        elif groups[0][0] == 'M' and groups[0][1] == 'R':
            sns.heatmap(corr_matrix, mask=mask, annot=True, center=0, square=True, linewidths=0.5, vmin=-1, vmax=1,
                        cmap='Spectral_r', xticklabels=quantitative_variables, ax=axes[1, 1])
        else:
            pass

    plt.show()













