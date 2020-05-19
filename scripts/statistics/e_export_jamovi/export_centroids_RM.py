import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == '__main__':

    path_df = os.path.join(DIR_OUT, 'derived_tables', 'centroids_iso.csv')
    df = pd.read_csv(path_df)
    subgroups = df.groupby('Hemisphere')
    L = subgroups.get_group('L')
    R = subgroups.get_group('R')

    subject_variables = ['Subject', 'Gender', 'Age_in_Yrs', 'AgeQ', 'Handedness', 'HandednessQ', 'Dexterity_AgeAdj',
                         'Strength_AgeAdj', 'PMAT24_A_CR', 'PMAT24_A_CR_Q', 'ICV']
    variables = ['Mesh_Area', 'Fiedler_Length', 'Roi_Area', 'Max_Geo_Depth', 'PP_CS_Coord_Iso', 'PP_Pre_Coord_Iso',
                 'PP_Post_Coord_Iso', 'PP_CS_Depth', 'Centroid_Diag_Coord_Iso', 'Centroid_Orth_Coord_Iso',
                 'Centroid_Diag_Coord_Aligned', 'Centroid_Orth_Coord_Aligned', 'Centroid_Pre_Coord_Iso',
                 'Centroid_Post_Coord_Iso',
                 'Centroid_Pre_Coord_Aligned', 'Centroid_Post_Coord_Aligned']

    L = L[subject_variables + variables + ['Label']]
    # shameless hack to avoid renamming when merging
    R = R[['Subject'] + variables]

    L_variables = [v + '_' + 'L' for v in variables]
    R_variables = [v + '_' + 'R' for v in variables]
    A_variables = [v + '_' + 'Asymmetry' for v in variables]

    d_L = {v: L_variables[i] for i, v in enumerate(variables)}
    d_R = {v: R_variables[i] for i, v in enumerate(variables)}

    L = L.rename(index=str, columns=d_L)
    L = L.reset_index(drop=True)
    R = R.rename(index=str, columns=d_R)
    R = R.reset_index(drop=True)

    print
    L.head()
    print
    R.head()

    final = pd.concat([L, R], axis=1)

    for i, v in enumerate(variables):
        R_v = final[R_variables[i]].values
        L_v = final[L_variables[i]].values
        A = 2 * (R_v - L_v) / (R_v + L_v)
        final[A_variables[i]] = A

    for label, subdf in final.groupby('Label'):
        subdf.to_csv(os.path.join(DIR_JAM, 'inter', 'centroids' + '_' + str(int(label)) + '_' + 'RM.csv'), index=False)
