"""
Helper to draw both Pre-central and Post-central gyral crests onto the grey matter/white matter
triangular meshes. This script should be launched into ipython interactive terminal

"""

import os
import anatomist.api as anatomist
from configuration.configuration import (
    MESHES,
    EXTREMITIES,
    GYRAL_CRESTS,
    SULCUS,
    ADJACENT_GYRI,
    SUBJ_LIST,
    SIDES,
)

subject = SUBJ_LIST[0]  # to be modified (0-99)
side = SIDES.keys()[0]  # to be modified (0-1)

path_mesh = MESHES[(subject, side)]
path_extremities = EXTREMITIES[(subject, side)]

# to handle the case of modification of existing lines
path_precentral = GYRAL_CRESTS[
    (subject, side, ADJACENT_GYRI[SULCUS][0], "drawn", "texture")
]
path_postcentral = GYRAL_CRESTS[
    (subject, side, ADJACENT_GYRI[SULCUS][1], "drawn", "texture")
]

if os.path.exists(path_precentral) and os.path.exists(path_postcentral):
    print(" Gyral crests are already drawn do you want to redo it ?")
else:
    a = anatomist.Anatomist()
    mesh = a.loadObject(path_mesh)
    mesh.setMaterial(polygon_mode="outline")
    ext = a.loadObject(path_extremities)
    ext.setPalette("Blue-Red-fusion")
    fusion = a.fusionObjects([mesh, ext], method="FusionTexSurfMethod")
    a.execute("TexturingParams", object=fusion, interpolation="rgb")
    w = a.createWindow("3D")
    w.addObjects(fusion)
