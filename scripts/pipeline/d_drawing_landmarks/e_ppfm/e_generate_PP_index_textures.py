import os
import numpy as np
import pandas as pd
from soma import aims
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES

if __name__ == '__main__':

    #we dont use pandas so that the code works even for BV4.5
    path_df = os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_mesh_index.csv')
    df = pd.read_csv(path_df)

    SUBJ_LIST = ['555651']
    SIDES = ['L']
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            index = int(df.loc[(df['Subject']== int(subject)) & (df['Hemisphere']== side),'Vertex' ])
            print index
            path_mesh = os.path.join(DIR_IN, subject + '_' + side + 'white.gii')
            path_pp_tex = os.path.join(DIR_OUT,'pli_passage','textures', subject + '_' + side + '_' + 'pli_passage.gii')
            mesh = aims.read(path_mesh)
            vertices = np.array(mesh.vertex())
            # print len(vertices)
            pp = np.zeros(vertices.shape[0],dtype=np.int16)
            pp[index] = 1
            pp_texture = aims.TimeTexture(pp)
            aims.write(pp_texture,path_pp_tex)

