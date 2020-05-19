import os
import numpy as np
import pandas as pd
from scipy.linalg import norm
from variables import DIR_IN, DIR_OUT

if __name__ == '__main__':

    path_df_in = os.path.join(DIR_OUT, 'derived_tables', 'centroids_iso.csv')
    path_df_in_1 = os.path.join(DIR_OUT, 'inter_tables', 'pp_new_coordinates.csv')
    df = pd.read_csv(path_df_in)
    df1 = pd.read_csv(path_df_in_1)

    # print df1
    df = df.dropna()
    df1 = df1[['Subject', 'Hemisphere', 'PP_Diag_Coord_Iso', 'PP_Diag_Coord_Aligned', 'PP_Orth_Coord_Iso',
               'PP_Orth_Coord_Aligned']]

    df_final = pd.merge(left=df, right=df1, on=['Subject', 'Hemisphere'])

    df_final['Centroid_PP_Diag_Diff_Iso'] = df_final['Centroid_Diag_Coord_Iso'] - df_final['PP_Diag_Coord_Iso']
    df_final['Centroid_PP_Diag_Diff_Aligned'] = df_final['Centroid_Diag_Coord_Aligned'] - df_final[
        'PP_Diag_Coord_Aligned']
    df_final['Centroid_PP_Orth_Diff_Iso'] = df_final['Centroid_Orth_Coord_Iso'] - df_final['PP_Orth_Coord_Iso']
    df_final['Centroid_PP_Orth_Diff_Aligned'] = df_final['Centroid_Orth_Coord_Aligned'] - df_final[
        'PP_Orth_Coord_Aligned']

    ##put it into the RM measurements format:

    df_final_L = df_final.loc[df['Hemisphere'] == 'L']
    df_final_R = df_final.loc[df['Hemisphere'] == 'R']

    df_final_L = df_final_L.rename(index=str, columns={'Centroid_PP_Diag_Diff_Iso': 'Centroid_PP_Diag_Diff_Iso_L',
                                                       'Centroid_PP_Diag_Diff_Aligned': 'Centroid_PP_Diag_Diff_Aligned_L',
                                                       'Centroid_PP_Orth_Diff_Iso': 'Centroid_PP_Orth_Diff_Iso_L',
                                                       'Centroid_PP_Orth_Diff_Aligned': 'Centroid_PP_Orth_Diff_Aligned_L'})
    df_final_R = df_final_R.rename(index=str, columns={'Centroid_PP_Diag_Diff_Iso': 'Centroid_PP_Diag_Diff_Iso_R',
                                                       'Centroid_PP_Diag_Diff_Aligned': 'Centroid_PP_Diag_Diff_Aligned_R',
                                                       'Centroid_PP_Orth_Diff_Iso': 'Centroid_PP_Orth_Diff_Iso_R',
                                                       'Centroid_PP_Orth_Diff_Aligned': 'Centroid_PP_Orth_Diff_Aligned_R'})
    df_final_RM = pd.merge(left=df_final_L, right=df_final_R, on=['Subject', 'Label'])
    print(df_final_RM)
    df_final_RM.to_csv(os.path.join(DIR_OUT, 'inter_tables', 'centroid_pp_diag_new_coordinate_RM.csv'))
    for label in [0, 1, 2, 3, 4]:
        df_final_label_RM = df_final_RM.loc[df_final_RM['Label'] == label]
        df_final_label_RM.to_csv(
            os.path.join(DIR_OUT, 'inter_tables', 'centroid_pp_diag_new_coordinate_RM_' + str(label) + '.csv'))

    # df_final.to_csv(os.path.join(DIR_OUT,'inter_tables','centroid_pp_diag_new_coordinate.csv'), index=False)
