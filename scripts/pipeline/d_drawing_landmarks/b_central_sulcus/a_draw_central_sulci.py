from __future__ import print_function
import os
import numpy as np
from soma import aims
from libs.tools.brainvisa import Xx
from configuration.configuration import EXTREMITIES, MESHES, DPFS, SUBJ_LIST, SIDES, CS_FUNDUS



if __name__ == '__main__':

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in SIDES:
            path_extremities = EXTREMITIES[subject, side]
            if os.path.exists(path_extremities):
                path_mesh = MESHES[subject, side]
                path_dpf = DPFS[subject, side]
                path_fundus_tex = CS_FUNDUS[subject,side,'texture']
                #sulcus fundus as mesh index list
                path_fundus_index = CS_FUNDUS[subject, side, 'array']

                #Get the two extremal points of the sulcus fundus line index
                ext_tex = aims.read(path_extremities)
                ext = np.array(ext_tex[0])
                #round the texture to avoid error when texture modified in SurfPaint
                ext = np.round(ext)
                start = np.where(ext == 50.00)[0][0]
                end = np.where(ext == 100.00)[0][0]
                mesh = aims.read(path_mesh)
                dpf = aims.read(path_dpf)
                #draw sulcus fundus line and retrieve ist vertices index on mesh
                sulcus = sulcus_fundus_from_extremities(start, end, mesh, dpf)
                np.save(path_fundus_index,sulcus)
                sulcus_tex = index_to_texture(sulcus,ext.shape[0])
                aims.write(sulcus_tex, path_fundus_tex)

            else:
                print("Extremities texture does not exists for subject  ", subject , side , ' Hemisphere')

