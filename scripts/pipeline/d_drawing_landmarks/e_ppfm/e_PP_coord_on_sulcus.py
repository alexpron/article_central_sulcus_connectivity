import os
import pandas as pd
import numpy as np
from configuration import DIR_OUT, SUBJ_LIST, SIDES

if __name__ == '__main__':


    path_df  = os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_mesh_index.csv')
    df = pd.read_csv(path_df)
    df['PP_CS_Coord_Iso'] = -1

    for i, subject in enumerate(SUBJ_LIST):
        for j , side in enumerate(SIDES):
            print subject, side
            path_sulcus = os.path.join(DIR_OUT, 'sulci', 'fundus', subject + '_' + side + '_' + 'central_sulcus.npy')
            path_param = os.path.join(DIR_OUT, 'sulci', 'fundus', subject + '_' + side + '_' + 'central_sulcus_iso_param.npy')
            sulcus = np.load(path_sulcus)
            param = np.load(path_param)
            vertex = df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side),'Vertex']
            print vertex.shape
            if vertex.shape[0]==1:
                vertex = int(vertex.values)
                ind = np.where(sulcus == vertex)
                coord = param[ind]
                if len(coord)==1:
                    df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_CS_Coord_Iso'] = coord
                else:
                    print "ERROOOR",subject , side , "VERTEX is not on the line"
            else:
                print "ERROR", subject, side, "NOT DRAWN ! "
    df.info()
    #recoding variables


    df.to_csv(os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_coord_sulcus.csv'))














