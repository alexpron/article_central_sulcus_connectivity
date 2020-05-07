"""

"""

import os
import numpy as np
import pandas as pd
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES, GYRI



if __name__ == '__main__':

    path_df = os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_index_gyri.csv')
    path_df_out = os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_coord_gyri.csv')
    df = pd.read_csv(path_df)
    df['PP_Pre_Coord_Iso'] = -1
    df['PP_Post_Coord_Iso'] = -1
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for k, gyrus in enumerate(GYRI):
                gyr_suffix = gyrus.replace('central', '')
                gyr_suffix = gyr_suffix.upper()[0] + gyr_suffix[1:]
                variable_in = 'PP' + '_' + gyr_suffix + '_' + 'Index_Line'
                variable_out = 'PP' + '_' + gyr_suffix + '_' + 'Coord_Iso'
                path_gyrus_param = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' + 'cleaned'
                                                + '_' +
                                                'iso_param' + '.npy')
                pp_index_gyrus = int(df.loc[(df['Subject']==int(subject)) & (df['Hemisphere']==side), variable_in])
                gyrus_param = np.load(path_gyrus_param)
                pp_coord = gyrus_param[pp_index_gyrus]
                df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), variable_out] = pp_coord

    df.to_csv(path_df_out)





