import os
import numpy as np
from soma import aims
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES



if __name__ == '__main__':

    for subject in SUBJ_LIST:
        for side in SIDES:
            path_fundus = os.path.join(DIR_OUT,'sulci', 'fundus', subject + '_' + side + '_' + 'central_sulcus.npy')
            if os.path.exists(path_fundus):
                fundus = np.load(path_fundus)
                print fundus
                fundus = fundus.astype(np.uint16)
                print fundus
                mesh = aims.read(os.path.join(DIR_IN, subject + '_' + side + 'white.gii'))
                vertices = np.array(mesh.vertex())
                t = np.zeros(vertices.shape[0])
                t[fundus] = 1
                tex = aims.TimeTexture(t)
                aims.write(tex, os.path.join(DIR_OUT,'sulci','fundus', subject + '_' + side + '_' + 'central_sulcus.gii'))
            else:
                print "Central sulcus fundus does not exist for subject ", subject, side, ' Hemisphere'






