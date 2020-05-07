"""
The pli de passage position along the central sulcus fundus is normally detected automatically using the
geodesic depth profile of the central sulcus. However some depth profiles does not allow to retrieve reliably
the PP position. For this case a manual drawing of the PP is performed using this script.

How to use this script ?



"""
from __future__ import print_function
import os
import numpy as np
from soma import aims
import anatomist.api as anatomist
from configuration import DIR_IN,DIR_OUT,SUBJ_LIST, SIDES, MESH


pof_L = {'boundingbox_max': [92.6499633789062, 69.6908569335938, 74.3419876098633],
 'boundingbox_min': [-88.2990188598633, -68.4405364990234, -78.5397796630859],
 'geometry': [0, 0, 1130, 970],
 'group': 0,
 'objects': [0, 5],
 'observer_position': [133.888809204102, 123.401985168457, 109.267555236816],
 'position': [134.719116210938, 108.979286193848, 116.38053894043, 0],
 'referential': 4,
 'selected': 0,
 'slice_quaternion': [0, 0, 0, 1],
 'type': 'AWindow',
 'view_quaternion': [0.301455736160278,
  0.105759382247925,
  0.920065522193909,
  0.226757511496544],
 'view_size': [1095, 886],
 'windowType': '3D',
 'zoom': 1.22140288352966}

pof_R = {'boundingbox_max': [90.2352752685547, 103.127212524414, 76.1187057495117],
 'boundingbox_min': [-99.5151138305664, -68.4468841552734, -122.21297454834],
 'geometry': [0, 0, 1130, 970],
 'group': 0,
 'objects': [0, 5],
 'observer_position': [103.698524475098, 108.235321044922, 131.373916625977],
 'position': [79.0391998291016, 107.622947692871, 117.274536132812, 0],
 'referential': 4,
 'selected': 0,
 'slice_quaternion': [0, 0, 0, 1],
 'type': 'AWindow',
 'view_quaternion': [0.303208589553833,
  -0.0535858757793903,
  -0.868557989597321,
  0.388329952955246],
 'view_size': [1095, 886],
 'windowType': '3D',
 'zoom': 2.22554111480713}


#Paths
wm_meshes = [os.path.join(DIR_IN, sub + '_' + side + MESH +'.gii') for sub in SUBJ_LIST for side in SIDES]
dpfs = [os.path.join(DIR_IN, sub + '_' + side + MESH +'_DPF.gii') for sub in SUBJ_LIST for side in SIDES]
curvatures = [os.path.join(DIR_IN, sub + '_' + side + '_' + MESH + '_curvature'
                                                                  '.gii') for sub in SUBJ_LIST for side in SIDES]
depths = [os.path.join(DIR_IN, sub + '_' + side + MESH +'_depth.gii') for sub in SUBJ_LIST for side in SIDES]

sulci = [os.path.join(DIR_OUT,'sulci','fundus', sub + '_' + side + '_' + 'central_sulcus.mesh') for sub in SUBJ_LIST
         for side in SIDES]
sulci_param = [os.path.join(DIR_OUT,'sulci', 'fundus', sub + '_' + side + '_' +
                                      'central_sulcus_iso_param.gii') for sub in SUBJ_LIST
         for side in SIDES]
pps = [os.path.join(DIR_OUT,'pli_passage', 'textures', sub + '_' + side + '_' +
                                      'pli_passage.gii') for sub in SUBJ_LIST
         for side in SIDES]
subs = [sub for sub in SUBJ_LIST for side in SIDES]
sides = [side for sub in SUBJ_LIST for side in SIDES]



a = anatomist.Anatomist()


w3d = a.createWindow('3D',geometry=pof_L['geometry'])
w3d2 = a.createWindow('3D',geometry=pof_L['geometry'])
w3d3 = a.createWindow('3D',geometry=pof_L['geometry'])
#w3d4 = a.createWindow('3D',geometry=pof_L['geometry'])

#INDEX A MODIFIER POUR LANCER LE SCRIPT SUR UN AUTRE SUJET
##########################################################
i = 156
##########################################################
w = wm_meshes[i]
dpf = dpfs[i]
curv = curvatures[i]
sulcus = sulci[i]
param = sulci_param[i]
pp = pps[i]

amesh = a.loadObject(w)

adpf = a.loadObject(dpf)
asulcus = a.loadObject(sulcus)
acurvature = a.loadObject(curv)
aparam = a.loadObject(param)


#display output
amesh.setMaterial(diffuse=[0.8, 0.8, 0.8, 1], polygon_mode='outline')
asulcus.setMaterial(diffuse=[1,0,0,1],line_width=15)
adpf.setPalette('Blue-Red',minVal=0.80, maxVal=1.80,absoluteMode=True)

fusion = a.fusionObjects(objects=[asulcus,aparam], method='FusionTexSurfMethod')
fusion_dpf = a.fusionObjects(objects=[amesh,adpf],method='FusionTexSurfMethod')
fusion_curvature = a.fusionObjects(objects=[amesh,acurvature], method='FusionTexSurfMethod')

if sides[i] == 'L':
   pof = pof_L
else:
    pof = pof_R
w1_objects = [amesh, asulcus]

if os.path.exists(pp):
    mesh = a.toAimsObject(amesh)
    vertices = np.array(mesh.vertex())
    pp_tex = aims.read(pp)
    pp_a = np.array(pp_tex[0])
    pp_ind = np.where(pp_a!=0)[0]
    v = vertices[pp_ind][0].tolist()
    pp_sphere = aims.SurfaceGenerator.sphere(v, 0.5, 200)
    a_pp = a.toAObject(pp_sphere)
    pp_material = a.Material(diffuse=[0,0,1,1]) #blue in RGB
    a_pp.setMaterial(pp_material)
    w1_objects.append(a_pp)

w3d.addObjects(w1_objects)
w3d2.addObjects([fusion_dpf])
w3d3.addObjects([fusion_curvature])
w3d.camera( view_quaternion=pof['view_quaternion'], zoom=pof['zoom'],slice_quaternion=pof['slice_quaternion'], observer_position=pof['observer_position'])
w3d2.camera( view_quaternion=pof['view_quaternion'], zoom=pof['zoom'],slice_quaternion=pof['slice_quaternion'],
             observer_position=pof['observer_position'])
w3d3.camera( view_quaternion=pof['view_quaternion'], zoom=pof['zoom'],slice_quaternion=pof['slice_quaternion'],
             observer_position=pof['observer_position'])













