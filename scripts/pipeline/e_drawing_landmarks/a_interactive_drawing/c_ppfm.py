"""
Helper to localise the pli de passage fronto-pariétal moyen (PPFM) of the central sulcus
 + the PPFM must be located along the central sulcus fundus line
 + the local elevation of the sulcal floor is spotted thanks to DPF and curvature surface maps.
"""
import anatomist.api as anatomist
from configuration.configuration import MESHES, DPFS, CURVATURES, SULCUS_FUNDI, SUBJ_LIST, SIDES

subject = SUBJ_LIST[0]  # to be modified (0-99)
side = SIDES.keys()[0]  # to be modified (0-1)

blue = [0, 0, 1, 1]
default = [0.8, 0.8, 0.8, 1]

a = anatomist.Anatomist()

windows = [a.createWindow('3D') for i in range(3)]

mesh = a.loadObject(MESHES[(subject, side)])
dpf = a.loadObject(DPFS[(subject, side)])
curvature = a.loadObject(CURVATURES[(subject, side)])
sulcus_fundus = a.loadObject(SULCUS_FUNDI[(subject, side, 'cleaned', 'texture')])

# display output
mesh.setMaterial(diffuse=default, polygon_mode='outline')
dpf.setPalette('Blue-Red', minVal=0.80, maxVal=1.80, absoluteMode=True)
curvature.setPalette('Blue-Red-fusion', maxVal=0, absoluteMode=True)
sulcus_fundus.setPalette('Blue-fusion', minVal=99, maxVal=100, absoluteMode=True)

fusion_dpf = a.fusionObjects(objects=[mesh, dpf], method='FusionTexSurfMethod')
fusion_curvature = a.fusionObjects(objects=[mesh, curvature], method='FusionTexSurfMethod')
fusion_fundus = a.fusionObjects(objects=[mesh, sulcus_fundus], method='FusionTexSurfMethod')

windows[0].addObjects([fusion_dpf])
windows[1].addObjects([fusion_curvature])
windows[2].addObjects([fusion_fundus])
