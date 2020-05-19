"""

"""
import os
import pandas as pd
from variables import DIR_OUT

if __name__ == '__main__':
    path_df_in = os.path.join(DIR_OUT, 'inter_tables', 'streamlines_level.csv')
    path_df_out = os.path.join(DIR_OUT, 'derived_tables', 'nb_streamlines_hemi_level.csv')
    df = pd.read_csv(path_df_in)
    df['Nb_Streamlines_Hemi'] = df.groupby(['Hemisphere', 'Subject'])['Age_in_Yrs'].transform('count')
    df = df.drop_duplicates(['Subject', 'Hemisphere'])
    # remove columns under hemisphere level
    df = df.drop(columns=['Label', 'Pre_Coord_Aligned', 'Pre_Coord_Iso', 'Post_Coord_Aligned', 'Post_Coord_Iso',
                          'Diag_Coord_Aligned', 'Orth_Coord_Aligned', 'Diag_Coord_Iso', 'Orth_Coord_Iso'])
    df.to_csv(path_df_out, index=False)
