import os
import numpy as np
from soma import aims
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES
from meshes_.processing import vertices_to_2d_line


if __name__ == '__main__':

    # SUBJ_LIST = ['144125', '346137', '196346', '598568', '147030','432332', '129129', '285345', '571144',
    #               '156637', '583858', '132017','189450']

    SUBJ_LIST = ['118730']
    SIDES = ['R']

    for subject in SUBJ_LIST:
        for side in SIDES:
            path_fundus = os.path.join(DIR_OUT,'sulci', 'fundus', subject + '_' + side + '_' + 'central_sulcus.npy')
            if os.path.exists(path_fundus):
                fundus = np.load(path_fundus)
                mesh = aims.read(os.path.join(DIR_IN, subject + '_' + side + 'white.gii'))
                vertices = np.array(mesh.vertex())
                vertices = vertices[fundus]
                line = vertices_to_2d_line(vertices)
                aims.write(line, os.path.join(DIR_OUT,'sulci','fundus', subject + '_' + side + '_' + 'central_sulcus.mesh'))
            else:
                print "Central sulcus fundus does not exist for subject ", subject, side, ' Hemisphere'






