"""

"""

import os
import numpy as np
import pandas as pd
from soma import aims, aimsalgo
from configuration.configuration import SUBJ_LIST, SIDES,  MESHES, SULCUS, ADJACENT_GYRI, PPFM_TABLES, GYRAL_CRESTS



if __name__ == '__main__':

    df = pd.read_csv(PPFM_TABLES['mesh_index'])
    df = df.dropna()
    df['PP_Pre_Index_Line'] = -1
    df['PP_Post_Index_Line'] = -1
    df['PP_Pre_Index_Brain'] = -1
    df['PP_Post_Index_Brain'] = -1


    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):

            mesh = aims.read(MESHES[(subject, side)])
            g = aims.GeodesicPath(mesh, 2, 2)
            vertices = np.array(mesh.vertex())
            pp_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'Vertex'])
            for k, gyrus in enumerate(ADJACENT_GYRI[SULCUS]):

                    #gyrus line as a set of white mesh index
                    gyrus_indexes = np.load(GYRAL_CRESTS[(subject, side, gyrus, 'cleaned', 'array')])
                    pp_gyr_index_brain, length = g.shortestPath_1_N_ind(pp_index, gyrus_indexes.tolist())
                    pp_gyr_index_line = np.where(gyrus_indexes == pp_gyr_index_brain)


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

    df.to_csv(PPFM_TABLES['gyrus_index'])










