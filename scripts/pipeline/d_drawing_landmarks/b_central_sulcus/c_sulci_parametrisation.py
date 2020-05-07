import os
import numpy as np
from soma import aims
from lines import normalized_curv_parametrisation
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES

if __name__ =='__main__':

    SUBJ_LIST = ['118730']
    SIDES = ['R']

    for subject in SUBJ_LIST:
        for side in SIDES:
            path_mesh = os.path.join(DIR_IN, subject + '_' + side + 'white.gii')
            path_fundus = os.path.join(DIR_OUT,'sulci', 'fundus', subject + '_' + side + '_' + 'central_sulcus.npy')
            path_param = os.path.join(DIR_OUT,'sulci', 'fundus', subject + '_' + side + '_' +
                                      'central_sulcus_iso_param.npy')
            path_param_tex = os.path.join(DIR_OUT,'sulci', 'fundus', subject + '_' + side + '_' +
                                      'central_sulcus_iso_param.gii')

            fundus_index = np.load(path_fundus)
            mesh = aims.read(path_mesh)
            vertices = np.array(mesh.vertex())
            fundus = vertices[fundus_index]
            norm_param = normalized_curv_parametrisation(fundus)
            norm_param_tex = aims.TimeTexture(norm_param)
            #print norm_param
            np.save(path_param,norm_param)
            aims.write(norm_param_tex, path_param_tex )


