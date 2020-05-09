import os
import numpy as np
from variables import SUBJ_LIST, SIDES, DIR_OUT, DIR_FIG
import pandas as pd
from pipeline.m_visualisation.visualisation import density_plot_subject, density_plot_subject_no_annot,density_plot_subject_no_annot_crests

sides = {'L': 'Left', 'R': 'Right'}

def get_hemisphere_group_pp(dataframe, subject, side):
    pre_c = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),'PP_Pre_Coord_Global_Mean'].iloc[0]
    post_c = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),'PP_Post_Coord_Global_Mean'].iloc[0]
    pp = np.array([pre_c, post_c])
    return pp
#
def get_hemisphere_subject_pp(dataframe,subject,side):
    """
    :param dataframe:
    :param subject:
    :param side:
    :param PP_coord:
    :return:
    """
    pre_coord = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),'PP_Pre_Coord_Iso'].iloc[0]
    post_coord = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),'PP_Post_Coord_Iso'].iloc[0]
    pp = np.array([pre_coord, post_coord])
    return pp




if __name__ == '__main__':
    names = ['global_mean'] #, 'global_mean', 'mean_by_hemi']
    factor = 5
    path_pli_passage = os.path.join(DIR_OUT,'drawing','ppfm','tables','pp_gyri.csv')
    path_X = os.path.join(DIR_OUT,'connectivity','densities', 'X.npy')
    path_Y = os.path.join(DIR_OUT,'connectivity','densities', 'Y.npy')
    pp = pd.read_csv(path_pli_passage)
    X = np.load(path_X)
    Y = np.load(path_Y)
    maxi = []
    SUBJ_LIST = ['114621']
    SIDES = ['L']
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):

           #print subject, side
           #
           subject_pp = get_hemisphere_subject_pp(pp,subject,side)
           #print subject_pp
           group_pp = get_hemisphere_group_pp(pp, subject, side)

           for k, name in enumerate(names):

                path_density = os.path.join(DIR_OUT,'connectivity','densities','subjects', name + '_' + subject + '_' + side
                                     + '_' + 'filtered' + '_' + 'radius' + '_' + str(factor) + '.npy')
                if os.path.exists(path_density):
                    density = np.load(path_density)
                    maxi.append(density.max())
                    #title = 'Central Sulcus Subject Connectivity Space'
                    title = None
                    # title = 'Central Sulcus Subject Connectivity Space: \n' + subject + ' ' + sides[side] + ' ' + \
                    #                                                                       'Hemisphere'
                    path_fig = os.path.join(DIR_FIG,'connectivity_space','densities','subjects', subject + '_' + side + \
                                                                                                                '_' +
                                            name + '_' +
                                        'radius' + '_' + str(factor) + '_group_pp_filtered_with_crests.tiff' )

                    density_plot_subject_no_annot_crests(X,Y,density,pli_passage_subject=subject_pp, pli_passage_group=None,
                                         path_fig=path_fig, title=title)
                else:
                    pass
                   # print "Density file does not exist"

