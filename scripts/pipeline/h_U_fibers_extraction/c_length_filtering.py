import os
import numpy as np
import pandas as pd
from configuration.configuration i

if __name__ == '__main__':
    THRESH = 100  # really long u-fibers

    df = pd.read_csv(os.path.join(DIR_OUT, 'connectivity', 'coordinates', 'raw', 'U_fibers_length.csv'))
    lengths = df['Length'].values
    length_filter = lengths < THRESH
    np.save(os.path.join(DIR_OUT, 'connectivity', 'length_filter.npy'), length_filter)
