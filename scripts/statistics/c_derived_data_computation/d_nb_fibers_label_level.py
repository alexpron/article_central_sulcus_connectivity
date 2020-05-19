"""

"""
import os
import pandas as pd
from variables import DIR_OUT

if __name__ == '__main__':
    path_df_in = os.path.join(DIR_OUT, 'inter_tables', 'streamlines_level.csv')
    path_df_out = os.path.join(DIR_OUT, 'derived_tables', 'nb_streamlines_label_level.csv')
    df = pd.read_csv(path_df_in)
    df['Nb_Streamlines_Label'] = df.groupby(['Hemisphere', 'Subject', 'Label'])['Age_in_Yrs'].transform('count')
    df = df.drop_duplicates(['Subject', 'Hemisphere', 'Label'])
    # remove columns under label level
    df = df.drop(
        columns=['Pre_Coord_Aligned', 'Pre_Coord_Iso', 'Post_Coord_Aligned', 'Post_Coord_Iso', 'Diag_Coord_Aligned',
                 'Orth_Coord_Aligned', 'Diag_Coord_Iso', 'Orth_Coord_Iso'])
    df.to_csv(path_df_out, index=False)
