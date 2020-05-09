import numpy as np
from soma import aims
from lines import normalized_curv_parametrisation
from configuration.configuration import SUBJ_LIST, SIDES, MESHES, CS_FUNDUS, CS_PARAM

if __name__ == '__main__':

    for subject in SUBJ_LIST:
        for side in SIDES:
            fundus_index = np.load(CS_FUNDUS[(subject, side,'cleaned','array')])
            mesh = aims.read(MESHES[(subject, side)])
            vertices = np.array(mesh.vertex())
            fundus = vertices[fundus_index]
            norm_param = normalized_curv_parametrisation(fundus)
            norm_param_tex = aims.TimeTexture(norm_param)
            np.save(CS_PARAM[(subject, side, 'iso','array')], norm_param)
            aims.write(norm_param_tex, CS_PARAM[(subject, side, 'iso', 'tex')])


