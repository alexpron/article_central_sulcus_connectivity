import os
import numpy as np
from variables import SIDES, DIR_OUT, DIR_FIG
import pandas as pd
from pipeline.m_visualisation.visualisation import density_plot_group

sides = {'L': 'Left', 'R': 'Right'}

if __name__ == '__main__':
    names = ['global_mean']
    factor = 5
    density_max = 8000
    path_pli_passage = os.path.join(DIR_OUT,'pli_passage','pp_gyri.csv')
    path_X = os.path.join(DIR_OUT,'connectivity','densities', 'X.npy')
    path_Y = os.path.join(DIR_OUT,'connectivity','densities', 'Y.npy')
    pp = pd.read_csv(path_pli_passage)
    X = np.load(path_X)
    Y = np.load(path_Y)


    for j, side in enumerate(SIDES):
        #extract the pli de passage coordinates
        pre_c = pp.loc[pp['Hemisphere']==side,'PP_Pre_Coord_Global_Mean'].iloc[0]
        post_c = pp.loc[pp['Hemisphere']==side,'PP_Post_Coord_Global_Mean'].iloc[0]
        pli = np.array([pre_c, post_c])
        pli=None

        for i, name in enumerate(names):

            path_density = os.path.join(DIR_OUT,'connectivity','densities','group', name + '_' + side + '_' +
                                 'filtered' + '_' + 'radius' + '_' + str(factor) + '.npy')
            if os.path.exists(path_density):
                density = np.load(path_density)

                title = 'CS Mean Connectivity Profile: \n' + sides[side] + ' ' + 'Hemisphere'
                path_fig = os.path.join(DIR_FIG,'connectivity_space','densities','group', side + '_' + name + '_' +
                                    'radius' + '_' + str(factor) + '_raw.png' )
                density_plot_group(X,Y, density, pli_passage=pli, path_fig=path_fig, title=title,vmin=0, vmax=density_max)
            else:
                pass
                #print "Density file does not exist"