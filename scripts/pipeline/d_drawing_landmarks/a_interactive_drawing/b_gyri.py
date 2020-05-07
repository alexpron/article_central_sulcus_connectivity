"""Draw

"""

from __future__ import print_function
import os
import anatomist.api as anatomist
from configuration import SUBJ_LIST, DIR_DATA,SIDES,MESH


#path of white meshes (left and right) were to draw the gyri
path_meshes = [os.path.join(DIR_DATA,subj + '_' + side + MESH + '.gii') for subj in SUBJ_LIST for side in SIDES]
path_extremities = [os.path.join(DIR_DATA,'drawn','extremities', subj + '_' + side + '_' +
                                 'central_sulcus_extremities_drawn.tex.gii') for subj in SUBJ_LIST for side in
                    SIDES]
#to handle the cas of modifications of existing lines
path_precentral = [os.path.join(DIR_DATA,'drawn','gyri', subj + '_' + side + '_' + 'precentral' + '_'
                                + 'drawn.tex.gii') for
                   subj in SUBJ_LIST for side in SIDES]
path_postcentral = [os.path.join(DIR_DATA,'drawn','gyri',  subj + '_' + side + '_' + 'postcentral_drawn.tex.gii') for
                    subj in SUBJ_LIST for side in SIDES]
#launching anatomist
a = anatomist.Anatomist()

i = 0

if os.path.exists(path_precentral[i]) and os.path.exists(path_postcentral[i]):
    print("Gyral crests are already drawn do you want to redo it ?")
else:
    mesh = a.loadObject(path_meshes[i])
    mesh.setMaterial(polygon_mode='outline')
    ext = a.loadObject(path_extremities[i])
    ext.setPalette('Blue-Red-fusion')
    fusion = a.fusionObjects([mesh,ext],method='FusionTexSurfMethod')
    a.execute("TexturingParams", object=fusion, interpolation='rgb')
    w1 = a.createWindow('3D')
    w1.addObjects(fusion)


