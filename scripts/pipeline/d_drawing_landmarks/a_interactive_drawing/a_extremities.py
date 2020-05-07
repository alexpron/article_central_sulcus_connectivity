"""Interactive script to draw the common extremities of the gyral and sulcal lines.

These points are drawn in each extremity of the central sulcus based on the grey/white interface mesh (geometry) and the
Depth Potential Function computed with default parameter. The script preload the fusion of the mesh and the dpf. Script is supposed to be launched into iPython

"""

import os
import anatomist.api as anatomist
from configuration import DIR_DATA, SUBJ_LIST, SIDES, MESH




#path of white meshes (left and right) were to draw the objects extremities
path_meshes = [os.path.join(DIR_DATA,'input', subject + '_' + side + MESH + '.gii') for \
        subject in
               SUBJ_LIST for side in SIDES]
path_dpfs = [os.path.join(DIR_DATA,'input', subject + '_' + side + MESH + '_DPF.gii') for \
        subject in SUBJ_LIST for side in SIDES]
#launching anatomist
a = anatomist.Anatomist()
w = a.createWindow('3D')
#the index of the hemisphere to draw (change this to get an other hemisphere)
hemisphere_index = 0
mesh = a.loadObject(path_meshes[hemisphere_index])
mesh.setMaterial(polygon_mode='outline')
dpf = a.loadObject(path_dpfs[hemisphere_index])
dpf.setPalette('Purple-Red + Stripes', minVal=0, maxVal=-1.6, absoluteMode=True)
fusion = a.fusionObjects(objects=[mesh, dpf], method='FusionTexSurfMethod')
w.addObjects(fusion)






