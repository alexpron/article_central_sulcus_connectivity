"""

"""

import os
import numpy as np
import pandas as pd
from soma import aims,aimsalgo
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES, GYRI



if __name__ == '__main__':

    df = pd.read_csv(os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_coord_sulcus.csv'))
    df = df.dropna()
    df['PP_Pre_Index_Line'] = -1
    df['PP_Post_Index_Line'] = -1
    df['PP_Pre_Index_Brain'] = -1
    df['PP_Post_Index_Brain'] = -1

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            path_mesh = os.path.join(DIR_IN, subject + '_' + side + 'white.gii')
            mesh = aims.read(path_mesh)
            g = aims.GeodesicPath(mesh,2,2)
            vertices = np.array(mesh.vertex())
            pp_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side),'Vertex' ])
            #pp = vertices[pp_index]
            for k, gyrus in enumerate(GYRI):

                    path_cleaned_gyrus = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                      'cleaned.npy')
                    #gyrus line as a set of white mesh index
                    gyrus_indexes = np.load(path_cleaned_gyrus)

                    pp_gyr_index_brain, length = g.shortestPath_1_N_ind(pp_index, gyrus_indexes.tolist())
                    pp_gyr_index_line = np.where(gyrus_indexes==pp_gyr_index_brain)

                    if gyrus == 'precentral':
                        df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side),'PP_Pre_Index_Line'] = pp_gyr_index_line
                        df.loc[(df['Subject'] == int(subject)) & (
                                    df['Hemisphere'] == side), 'PP_Pre_Index_Brain'] = pp_gyr_index_brain

                    elif gyrus == 'postcentral':
                        df.loc[(df['Subject'] == int(subject)) & (
                                    df['Hemisphere'] == side), 'PP_Post_Index_Line'] = pp_gyr_index_line
                        df.loc[(df['Subject'] == int(subject)) & (
                                df['Hemisphere'] == side), 'PP_Post_Index_Brain'] = pp_gyr_index_brain
                    else:
                        pass
    df.to_csv(os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_index_gyri_geo_weight_curv_2.csv'))











