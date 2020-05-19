import os
import numpy as np
import pandas as pd
from scipy.linalg import norm
from variables import DIR_IN, DIR_OUT

if __name__ == '__main__':
    path_df_in = os.path.join(DIR_OUT, 'inter_tables', 'coordinates.csv')
    df = pd.read_csv(path_df_in)

    hemisphere_level = pd.read_csv(os.path.join(DIR_OUT, 'inter_tables', 'hemispheres_level.csv'))

    df['Centroid_Diag_Coord_Iso'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')['Diag_Coord_Iso']
    df['Centroid_Orth_Coord_Iso'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')['Orth_Coord_Iso']
    df['Centroid_Diag_Coord_Aligned'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')[
        'Diag_Coord_Aligned']
    df['Centroid_Orth_Coord_Aligned'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')[
        'Orth_Coord_Aligned']
    df['Centroid_Pre_Coord_Iso'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')['Pre_Coord_Iso']
    df['Centroid_Post_Coord_Iso'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')['Post_Coord_Iso']
    df['Centroid_Pre_Coord_Aligned'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')[
        'Pre_Coord_Aligned']
    df['Centroid_Post_Coord_Aligned'] = df.groupby(['Hemisphere', 'Subject', 'Label']).transform('mean')[
        'Post_Coord_Aligned']
    new_df = df.drop_duplicates(['Subject', 'Hemisphere', 'Label'])
    new_df = new_df.loc[df['Label'] != -1]

    final_df = pd.merge(hemisphere_level, new_df, on=['Subject', 'Hemisphere'])

    final_df = final_df.sort_values(['Subject', 'Hemisphere', 'Label'])
    # print final_df.head()
    final_df.to_csv(os.path.join(DIR_OUT, 'derived_tables', 'centroids_iso.csv'), index=False)
