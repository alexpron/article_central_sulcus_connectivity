import os
import pandas as pd
from variables import DIR_JAM

if __name__ == '__main__':
    for label in ['0', '1', '2', '3', '4']:
        df1 = pd.read_csv(os.path.join(DIR_JAM, 'centroids_' + label + '.csv'))
        df2 = pd.read_csv(os.path.join(DIR_JAM, 'nb_streamlines_label_level_' + label + '.csv'))
        df2 = df2[['Subject', 'Hemisphere', 'Nb_Streamlines_Label']]
        df = pd.merge(df1, df2, on=['Subject', 'Hemisphere'])
        df.to_csv(os.path.join(DIR_JAM, 'whole_label_level_' + str(label) + '.csv'), index=False)
