import os
import numpy as np
import pandas as pd
from variables import SUBJ_LIST, SIDES, DIR_OUT, DIR_FIG
from pipeline.m_visualisation.visualisation import scatter_plot

def get_hemisphere_subject_pp(dataframe,subject,side,PP_coord):
    """
    :param dataframe:
    :param subject:
    :param side:
    :param PP_coord:
    :return:
    """
    subject_df = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),['Gyrus',
                               PP_coord ]]
    pre = subject_df.loc[subject_df['Gyrus'] == "precentral", [PP_coord]]
    pre_c = pre.iloc[0][0]
    post = subject_df.loc[subject_df['Gyrus'] == "postcentral", [PP_coord]]
    post_c = post.iloc[0][0]
    pp = np.array([pre_c, post_c])
    return pp


if __name__ == '__main__':
    d = 'global_mean'
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')
    #use iso (i.e coordinates without alignement on group pli de passage)
    path_data = os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'length_filtered', 'U_fibers_coord_iso.npy')
    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index_filtered.npy')
    path_pli_passage = os.path.join(DIR_OUT, 'pli_passage', 'pli_passage_coord_on_gyri.csv')
    pli_passage = pd.read_csv(path_pli_passage)
    data = np.load(path_data)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index,2)


    #remove streamlines considered as noise

    for j, side in enumerate(SIDES):
        path_labels = os.path.join(DIR_OUT,'group_clustering','dbscan_fixed','cluster_spreading','clusters', side + '.npy')
        labels = np.load(path_labels)
        for i, subject in enumerate(SUBJ_LIST):

            labels = np.load(path_labels)
            index = i*len(SIDES) + j
            data_ = data[hemispheres_index == index]
            labels_ = labels[hemispheres_index[side_index==j]==index]

            title = 'Group clusters on subject ' + subject + '_' + side + ' space \n  Noise kept'
            subject_pp = get_hemisphere_subject_pp(pli_passage, subject, side, 'PP_Iso_coord')
            path_fig = os.path.join(DIR_FIG,'connectivity_space','group_clustering','subjects_space',
                                    subject + '_' + side + 'extended_with_noise' +
                                    '.png' )
            scatter_plot(data_,labels_, title=title,pli_passage=subject_pp, path_fig=path_fig, colormap='dbscan')







