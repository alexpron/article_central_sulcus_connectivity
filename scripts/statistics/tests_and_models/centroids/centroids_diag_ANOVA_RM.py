import os
import pandas as pd
from variables import DIR_OUT
import numpy as np

if __name__ == '__main__':
    path_df1 = os.path.join(DIR_OUT, 'derived_tables', 'centroids_iso.csv')
    df1 = pd.read_csv(path_df1)
    print
    df1
    path_df2 = os.path.join(DIR_OUT, 'inter_tables', 'hemispheres_level.csv')
    df2 = pd.read_csv(path_df2)
    print
    df2
    # subjects = df2.drop_duplicates(subset='Subject')
    # subjects = subjects.iloc[:,:11]
    #
    # df = pd.merge(df1, df2, on=['Subject', 'Hemisphere'])
    # subgroups = df.groupby('Hemisphere')
    # L = subgroups.get_group('L')
    # L = L.rename(index=str,columns={'Centroid_Diag_Coord_Iso':'Centroid_Diag_Coord_Iso_L','Centroid_Orth_Coord_Iso':'Centroid_Orth_Coord_Iso_L'})
    # R = subgroups.get_group('R')
    # R = R.rename(index=str,columns={'Centroid_Diag_Coord_Iso':'Centroid_Diag_Coord_Iso_R','Centroid_Orth_Coord_Iso':'Centroid_Orth_Coord_Iso_R'})
    # new_df = pd.merge(L, R, on='Subject')
    # new_df = new_df.rename(index=str, columns={'Label_x':'Label'})
    # new_df = new_df[['Subject','Centroid_Diag_Coord_Iso_L','Centroid_Diag_Coord_Iso_R','Centroid_Orth_Coord_Iso_L','Centroid_Orth_Coord_Iso_R','Label']]
    # final_df = pd.merge(subjects, new_df, on='Subject')
    # sublabels = final_df.groupby('Label')
    # for label, labeldf in sublabels:
    #     print label
    #     labeldf.to_csv('/home/alex/test_anova_rm' + '_' + str(label) + '.csv')
