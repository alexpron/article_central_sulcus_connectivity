"""
Alternative scripts to compute triangular white mesh area. In the study, surface white mesh area was get manually through
the BrainVISA process of the cortical surface toolbox but this script is set there for the sake of completness
Area was computed for the white mesh in Aims diffusion space
"""

import pandas as pd
from soma import aims, aimsalgo


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, MESHES, MESH_AREA_DF

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
    df = pd.DataFrame({'Subject': subjects, 'Hemisphere': hemispheres, 'Mesh_Area': areas})
    df.to_csv(MESHES)
