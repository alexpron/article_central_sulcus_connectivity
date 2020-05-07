import os
import numpy as np
import pandas as pd
from soma import aims
from configuration import SUBJ_LIST, SIDES, DIR_PP, DIR_IN, DIR_OUT

if __name__ == '__main__':

    path_df = os.path.join(DIR_OUT,'pli_passage', 'tables', 'pp_manual_drawing_coord_gyri.csv')
    path_df_out = os.path.join(DIR_OUT,'pli_passage', 'tables', 'pp_manual_drawing_geo_depth.csv')
    df = pd.read_csv(path_df)
    df = df.rename(index=str, columns={'Vertex':'PP_CS_Index_Brain'})
    df['PP_CS_Depth'] = np.nan


    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):

            pp_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side),'PP_CS_Index_Brain'])
            path_depth = os.path.join(DIR_IN, subject + '_' + side + 'white' + '_' + 'depth.gii')
            depth_t = aims.read(path_depth)
            depth = np.array(depth_t[0])
            pp_depth = depth[pp_index]
            df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_CS_Depth'] = pp_depth

    df.to_csv(path_df_out, index=False)









