import os
import pandas as pd
from variables import DIR_OUT

if __name__ == '__main__':
    path1_in = os.path.join(DIR_OUT, 'inter_tables', 'coordinates.csv')
    path2_in = os.path.join(DIR_OUT, 'inter_tables', 'hemispheres_level.csv')
    path_out = os.path.join(DIR_OUT, 'inter_tables', 'streamlines_level.csv')
    d1 = pd.read_csv(path1_in)
    d2 = pd.read_csv(path2_in)
    stream_level = pd.merge(d1, d2, on=['Subject', 'Hemisphere'])
    stream_level.to_csv(path_out, index=False)
