import os
import pandas as pd
from variables import DIR_JAM

if __name__ == '__main__':
    for label in ['0', '1', '2', '3', '4']:
        df1 = pd.read_csv(os.path.join(DIR_JAM, 'inter', 'centroids_' + label + '_RM.csv'), index_col=0)
        df2 = pd.read_csv(os.path.join(DIR_JAM, 'inter', 'nb_streamlines_label_level_' + label + '_RM.csv'))
        # print df2.columns
        df2 = df2[['Subject', 'Nb_Streamlines_Label_L', 'Nb_Streamlines_Label_R', 'Nb_Streamlines_Label_Asymmetry']]
        df = pd.merge(df1, df2, on=['Subject'])
        print
        df.shape
        # print df.head()
        df.to_csv(os.path.join(DIR_JAM, 'whole_label_level_' + str(label) + '_RM.csv'), index=False)
