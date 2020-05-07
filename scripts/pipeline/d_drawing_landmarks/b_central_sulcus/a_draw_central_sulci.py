import os
import numpy as np
from soma import aims
from configuration import DIR_IN, DIR_OUT, DIR_EXT, SUBJ_LIST,  SIDES
#Project with Olivier's code dedicated to line on mesh drawing, cleaning and parametrisation
from lines import sulcus_fundus_from_extremities


def index_to_texture(index, texture_size,value=100):
    """
    :param index:
    :param texture_size:
    :param value:
    :return: AimsTimeTexture
    """
    t = np.zeros(texture_size)
    t[index]= value
    texture = aims.TimeTexture(t)
    return texture


if __name__ == '__main__':

    # SUBJ_LIST = ['144125', '346137', '196346', '598568', '147030','432332', '129129', '285345', '571144',
    #               '156637', '583858', '132017','189450']
    SUBJ_LIST = ['118730']
    SIDES = ['R']

    for i, sub in enumerate(SUBJ_LIST):
        for side in SIDES:
            path_extremities = os.path.join(DIR_EXT, sub + '_' + side + '_' + 'central_sulcus' + '_' +'extremities_drawn.tex.gii')
            if os.path.exists(path_extremities):
                path_mesh = os.path.join(DIR_IN, sub + '_' + side + 'white.gii')
                path_dpf = os.path.join(DIR_IN, sub + '_' + side + 'white_DPF.gii')
                #sulcus fundus as texture
                path_fundus_tex = os.path.join(DIR_OUT,'sulci','fundus', sub + '_' + side + '_' + 'central_sulcus.gii')
                #sulcus fundus as mesh index list
                path_fundus_index = os.path.join(DIR_OUT,'sulci','fundus', sub + '_' + side + '_' +
                                           'central_sulcus.npy')

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
                sulcus = sulcus_fundus_from_extremities(start,end,mesh,dpf)
                np.save(path_fundus_index,sulcus)
                sulcus_tex = index_to_texture(sulcus,ext.shape[0])
                aims.write(sulcus_tex, path_fundus_tex)

            else:
                print "Extremities texture does not exists for subject  ", sub , side , ' Hemisphere'

