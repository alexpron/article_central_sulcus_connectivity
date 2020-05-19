import os
import pandas as pd
from variables import DIR_OUT


if __name__ == '__main__':

    path_df1 = os.path.join(DIR_OUT,'inter_tables','subjects.csv')
    path_df2 = os.path.join(DIR_OUT,'init_tables','ICV.csv')
    path_df_out = os.path.join(DIR_OUT,'inter_tables','subjects_level.csv')

    df1 = pd.read_csv(path_df1,index_col=0)
    df2 = pd.read_csv(path_df2,index_col=0)

    df = pd.merge(df1,df2,on='Subject')

    df.to_csv(path_df_out)


