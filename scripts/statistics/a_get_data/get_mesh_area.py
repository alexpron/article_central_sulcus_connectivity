import os
import pandas as pd
from soma import aims, aimsalgo
from configuration.configuration import SUBJ_LIST, SIDES, MESHES



if __name__ == '__main__':

    subjects = []
    hemispheres = []
    areas = []
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            mesh = aims.read(MESHES[(subject, side, 'white')])
            area = aims.SurfaceManip.meshArea(mesh)
            subjects.append(int(subject))
            hemispheres.append(side)
            areas.append(area)
    df = pd.DataFrame({'Subject': subjects, 'Hemisphere': hemispheres, 'Area': areas})
    df.to_csv(os.path.join(DIR_OUT,'mesh_area.csv'))
