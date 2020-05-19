import os
import numpy as np
import pandas as pd
from variables import SUBJ_LIST, SIDES, DIR_OUT, DIR_FIG
from pipeline.m_visualisation.visualisation import scatter_plot

def get_hemisphere_subject_pp(dataframe,subject,side):
    """
    :param dataframe:
    :param subject:
    :param side:
    :param PP_coord:
    :return:
    """
    subject_df = dataframe.loc[(dataframe['Subject'] == int(subject)) & (dataframe['Hemisphere'] == side),['PP_Pre_Coord_Iso','PP_Post_Coord_Iso']]
    pre = subject_df['PP_Pre_Coord_Iso']
    print pre
    pre_c = pre.values
    print pre_c
    post = subject_df['PP_Post_Coord_Iso']
    post_c = post.values
    print post_c
    pp = np.array([pre_c, post_c])
    print "toto", pp
    return pp


if __name__ == '__main__':
    d = 'global_mean'
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')
    # use iso (i.e coordinates without alignement on group pli de passage)
    path_data = os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'length_filtered', 'U_fibers_coord_iso.npy')
    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index_filtered.npy')
    path_pli_passage = os.path.join(DIR_OUT, 'pli_passage', 'pp_gyri.csv')
    pli_passage = pd.read_csv(path_pli_passage)
    data = np.load(path_data)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index, 2)

    for j, side in enumerate(SIDES):
        labels = np.load(os.path.join(dir_output, d + '_' + 'all_labels' + '_' + side + '.npy'))
        data_ = data[side_index == j]
        labels_ = labels
        hemi_index = hemispheres_index[side_index == j]


        for i, subject in enumerate(SUBJ_LIST):
            index = i * len(SIDES) + j
            data_sub = data_[hemi_index == index]
            labels_sub = labels_[hemi_index == index]

            title = 'Group clusters on subject ' + subject + '_' + side + ' space '
            subject_pp = get_hemisphere_subject_pp(pli_passage, subject, side)
            path_fig = os.path.join(DIR_FIG, 'connectivity_space', 'group_clustering', 'subjects_space',
                                    subject + '_' + side +
                                    '_with_noise.png')
            print subject_pp
            scatter_plot(data_sub, labels_sub, title=title, pli_passage=subject_pp, path_fig=path_fig,
                         colormap='dbscan')





