import os
import numpy as np
import pandas as pd
from configuration import SUBJ_LIST, SIDES, DIR_DRAWN,DIR_DATA, DIR_OUT


path_df = os.path.join(DIR_DRAWN, 'pli_passage','pp_manual_drawing.csv')
df = pd.read_csv(path_df)
df = df[['Subject','Hemisphere','Vertex','Drawer']]
#keep only one examplar of the drawing (preferentially Olivier's one
df_final = df.drop_duplicates(['Subject','Hemisphere'])
df_final = df_final.reset_index(drop=True)
df_final['Vertex'] = df_final['Vertex'].astype(float)
df_final.to_csv(os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_mesh_index.csv'))


