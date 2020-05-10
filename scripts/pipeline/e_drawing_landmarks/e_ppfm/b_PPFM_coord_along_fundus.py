import os
import pandas as pd
import numpy as np
from configuration.configuration import SUBJ_LIST, SIDES, PPFM_TABLES, SULCUS_FUNDI, PARAMETRISATIONS

if __name__ == '__main__':



    df = pd.read_csv(PPFM_TABLES['mesh_index'])
    df['PP_CS_Coord_Iso'] = -1

    for i, subject in enumerate(SUBJ_LIST):
        for j , side in enumerate(SIDES):
            sulcus_fundus = np.load(SULCUS_FUNDI[(subject, side, 'cleaned','array')])
            param = np.load(PARAMETRISATIONS[(subject, side, 'CS', 'cleaned', 'iso', 'array')])
            vertex = df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side),'Vertex']
            if vertex.shape[0] == 1:
                vertex = int(vertex.values)
                ind = np.where(sulcus_fundus == vertex)
                coord = param[ind]
                if len(coord) == 1:
                    df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_CS_Coord_Iso'] = coord
                else:
                    print("Error", subject , side , "PPFM vertex is not on the CS fundus line")
            else:
                print("ERROR", subject, side, "NOT DRAWN !")

    df.to_csv(PPFM_TABLES['cs_coord'])














