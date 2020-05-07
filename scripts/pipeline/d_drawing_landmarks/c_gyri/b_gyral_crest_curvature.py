import os
import numpy as np
from soma import aims

from configuration import DIR_OUT,SUBJ_LIST,SIDES,GYRI


if __name__ == '__main__':

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for k, gyrus in enumerate(GYRI):
                 path_gyrus = os.path.join(DIR_OUT, 'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                     'cleaned.mesh')
                 gyral_crest = aims.read(path_gyrus)
                 vertices = np.array(gyral_crest.vertex())
                 T,N,B, curv, tors = frenet_serret(vertices)
                 curv_tex = aims.TimeTexture(curv)
                 tors_tex = aims.TimeTexture(tors)
                 print curv.shape
                 print tors.shape
                 aims.write(curv_tex,os.path.join(DIR_OUT, 'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                     'curvature.gii') )
                 aims.write(tors_tex,os.path.join(DIR_OUT, 'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                     'torsion.gii'))

