import os
from libs.tools.brainvisa import compute_surfacic_curvature
from configuration import SUBJ_LIST, SIDES, DIR_IN



if __name__ == '__main__':

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            name = subject + '_' + side
            path_mesh = os.path.join(DIR_IN, name + 'white.gii')
            path_curvature = os.path.join(DIR_IN, name + '_' + 'white' + '_' + 'curvature.gii')
            compute_surfacic_curvature(path_mesh, path_curvature)


