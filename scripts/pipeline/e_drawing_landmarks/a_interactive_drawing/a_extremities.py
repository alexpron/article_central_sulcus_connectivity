"""Interactive script to draw the common extremities of the gyral and sulcal lines.

These points are drawn in each extremity of the central sulcus based on the grey/white interface mesh (geometry) and the
Depth Potential Function computed with default parameter. The script preload the fusion of the mesh and the dpf. Script is supposed to be launched into iPython
"""

import anatomist.api as anatomist
from configuration.configuration import MESHES, DPFS, SUBJ_LIST, SIDES

subject = SUBJ_LIST[0]  # to be modified (0-99)
side = SIDES.keys()[0]  # to be modified (0-1)

path_mesh = MESHES[(subject, side)]
path_dpf = DPFS[(subject, side)]

a = anatomist.Anatomist()
w = a.createWindow("3D")
mesh = a.loadObject(path_mesh)
dpf = a.loadObject(path_dpf)
mesh.setMaterial(polygon_mode="outline")
dpf.setPalette("Purple-Red + Stripes", minVal=0, maxVal=-1.6, absoluteMode=True)
fusion = a.fusionObjects(objects=[mesh, dpf], method="FusionTexSurfMethod")
w.addObjects(fusion)
