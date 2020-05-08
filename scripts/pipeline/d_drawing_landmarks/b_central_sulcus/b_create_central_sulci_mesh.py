import os
import numpy as np
from soma import aims
from meshes_.processing import vertices_to_2d_line
from configuration.configuration import SUBJ_LIST, SIDES, CS_FUNDUS, MESHES


if __name__ == '__main__':

    for subject in SUBJ_LIST:
        for side in SIDES:
            path_fundus = CS_FUNDUS[subject, side, 'array']
            if os.path.exists(path_fundus):
                fundus = np.load(path_fundus)
                mesh = MESHES[subject, side]
                vertices = np.array(mesh.vertex())
                vertices = vertices[fundus]
                line = vertices_to_2d_line(vertices)
                aims.write(line, CS_FUNDUS[subject,side,'mesh'])
            else:
                print("Central sulcus fundus does not exist for subject ", subject, side, ' Hemisphere')






