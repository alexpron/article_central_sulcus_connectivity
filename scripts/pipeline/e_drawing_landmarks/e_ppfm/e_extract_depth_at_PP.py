import numpy as np
import pandas as pd
from soma import aims

if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, DEPTHS, PPFM_TABLES

    df = pd.read_csv(PPFM_TABLES['mesh_index'])
    df = df.rename(index=str, columns={'Vertex': 'PP_CS_Index_Brain'})
    df['PP_CS_Depth'] = np.nan

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            pp_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_CS_Index_Brain'])
            depth_t = aims.read()
            depth = np.array(depth_t[0])
            pp_depth = depth[pp_index]
            df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_CS_Depth'] = pp_depth

    df.to_csv(PPFM_TABLES['final'], index=False)
