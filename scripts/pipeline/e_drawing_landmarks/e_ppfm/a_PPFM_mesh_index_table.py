"""
Synthetize drawn pli de passage fronto-parietal moyen (PPFM) position along the central sulcus
fundus and keep the cleaner version (always chose Olivier's)
"""

import pandas as pd
from configuration.configuration import PPFM_TABLES

if __name__ == '__main__':
    df = pd.read_csv(PPFM_TABLES['draw_attribution'])
    df = df[['Subject', 'Hemisphere', 'Vertex', 'Drawer']]
    # keep only one examplar of the drawing (preferentially Olivier's one)
    df_final = df.drop_duplicates(['Subject', 'Hemisphere'])
    df_final = df_final.reset_index(drop=True)
    df_final['Vertex'] = df_final['Vertex'].astype(float)
    df_final.to_csv(PPFM_TABLES['mesh_index'])
