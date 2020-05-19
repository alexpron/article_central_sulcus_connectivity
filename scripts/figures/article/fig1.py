import os
import numpy as np
import pandas as pd
from soma import aims, aimsalgo
import anatomist.api as anatomist
from configuration.configuration import VISU_SUBJECT, VISU_SIDE

# CONSTANTS
R = 1  # radius in mm of the sphere to display
V = 200  # number of vertices of the sphere


def index_to_sphere(mesh, index, radius=R, nb_vertices=V):
    """
    Create a sphere of center the index th vertices of a mesh and of radius radius
    :param mesh:
    :param index:
    :param radius:
    :param nb_vertices:
    :return:
    """
    vertices = np.array(mesh.vertex())
    center = vertices[index]
    sphere = aims.SurfaceGenerator.sphere(aims.Point3df(center), radius, int(nb_vertices))
    return sphere


if __name__ == '__main__':

    subject = VISU_SUBJECT
    side = VISU_SIDE

    # COLORS
    white = [255, 255, 255]
    red_n = [1, 0, 0, 1]
    orange = [225, 140, 0]
    orange_n = [0.88, 0.549, 0, 1]
    purple = [153, 50, 204]
    purple_n = [0.6, 0.196, 0.8, 1]
    blue = [0, 0, 1, 1]
    yellow = [0.8, 0.8, 0.30, 1]
    default = [0.8, 0.8, 0.8, 1]
    modified = default[:-1] + [0.5]

    # colors for the precentral line
    orange_colors = []
    orange_colors.extend(white)
    for i in range(255):
        orange_colors.extend(orange)
    # colors for the postcentral line
    purple_colors = []
    purple_colors.extend(white)
    for i in range(255):
        purple_colors.extend(purple)

    # manually chosen point of view (works fine) only for chosen subject and hemisphere

    pov = {'boundingbox_max': [33.3758850097656, 52.2809677124023, 84.0576782226562],
           'boundingbox_min': [-33.3758926391602, -52.2809677124023, -84.0411911010742],
           'geometry': [123, 85, 419, 470],
           'group': 0,
           'objects': [6, 0],
           'observer_position': [120.531845092773, 106.553100585938, 95.2683334350586],
           'position': [140.520202636719, 103.752319335938, 81.4079055786133, 0],
           'referential': 10,
           'selected': 0,
           'slice_quaternion': [0, 0, 0, 1],
           'type': 'AWindow',
           'view_quaternion': [0.455769926309586,
                               0.350308388471603,
                               0.561817646026611,
                               0.594910860061646],
           'view_size': [384, 384],
           'windowType': '3D',
           'zoom': 1}

    path_mesh = VISU_MESH
    mesh = aims.read(path_mesh)
    path_pre_roi = os.path.join(DIR_ROIS, subject + '_' + side + '_' + 'precentral.gii')
    path_post_roi = os.path.join(DIR_ROIS, subject + '_' + side + '_' + 'postcentral.gii')
    path_pre_crest = os.path.join(DIR_CRESTS, VISU_ID + '_' + 'precentral_cleaned.gii')
    path_post_crest = os.path.join(DIR_CRESTS, VISU_ID + '_' + 'postcentral_cleaned.gii')
    path_pre_line = os.path.join(DIR_CRESTS, VISU_ID + '_' + 'precentral_cleaned.mesh')
    path_post_line = os.path.join(DIR_CRESTS, VISU_ID + '_' + 'postcentral_cleaned.mesh')
    df = pd.read_csv(PPFM)
    pp_pre_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_Pre_Index_Brain'])
    pp_post_index = int(df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side), 'PP_Post_Index_Brain'])
    pp_pre_sphere = index_to_sphere(mesh, pp_pre_index)
    pp_post_sphere = index_to_sphere(mesh, pp_post_index)

    a = anatomist.Anatomist()
    # remove anatomist cursor in all windows
    a.config()['linkedCursor'] = 0

    # custom palettes
    orange_palette = a.createPalette('PreCG')
    orange_palette.setColors(colors=orange_colors)
    purple_palette = a.createPalette('PoCG')
    purple_palette.setColors(colors=purple_colors)

    # create a windows for each sub-component of the figure
    mesh_with_cs = a.createWindow('3D')
    cs_landmarks = a.createWindow('3D')
    cs_rois = a.createWindow('3D')
    raw_tractogram = a.createWindow('3D')
    filtered_tractogram = a.createWindow('3D')
    association_fibers = a.createWindow('3D')
    u_fibers = a.createWindow('3D')

    windows = [mesh_with_cs, cs_landmarks, cs_rois, raw_tractogram, filtered_tractogram, association_fibers, u_fibers]
    # set identical point-of-view accross all windows
    for w in windows:
        w.camera(view_quaternion=pov['view_quaternion'], zoom=pov['zoom'], slice_quaternion=pov['slice_quaternion'],
                 observer_position=pov['observer_position'])

    # #loading objects (two identical meshes for two different windows)
    amesh1 = a.loadObject(path_mesh)
    amesh2 = a.loadObject(path_mesh)

    # surfacic rois
    pre_roi = a.loadObject(path_pre_roi)
    post_roi = a.loadObject(path_post_roi)

    # gyral crests
    # as textures
    pre = a.loadObject(path_pre_crest)
    post = a.loadObject(path_post_crest)
    # as lines
    pre_line = a.loadObject(path_pre_line)
    post_line = a.loadObject(path_post_line)

    # PPFM spheres
    a_pp_pre_sphere = a.toAObject(pp_pre_sphere)
    a_pp_post_sphere = a.toAObject(pp_post_sphere)

    # CS Object
    cs = a.loadObject(path_cs_object)

    # fibers
    tractogram = a.loadObject()
    filt_tractogram = a.loadObject()
    # association_streamlines = a.loadObject()
    u_fibers = a.loadObject(os.path.join()

    # #setting materials and palettes
    amesh1.setMaterial(diffuse=default, polygon_mode='normal')  # default grey mesh with outline style 'outline'
    amesh2.setMaterial(diffuse=modified, polygon_mode='normal')
    cs.setMaterial(diffuse=yellow)
    a_pp_pre_sphere.setMaterial(diffuse=blue)
    a_pp_post_sphere.setMaterial(diffuse=blue)
    pre_line.setMaterial(diffuse=orange_n)
    post_line.setMaterial(diffuse=purple_n)

    pre_roi.setPalette('PreCG', minVal=0.70)
    post_roi.setPalette('PoCG', minVal=0.70)
    pre.setPalette('PreCG', minVal=0.70)
    post.setPalette('PoCG', minVal=0.70)

    # #Fusions
    multitex_rois = a.fusionObjects(objects=[pre_roi, post_roi], method='FusionMultiTextureMethod')
    multitex_crests = a.fusionObjects(objects=[pre, post], method='FusionMultiTextureMethod')

    fusion_rois = a.fusionObjects(objects=[amesh1, multitex_rois], method='FusionTexSurfMethod')
    fusion_crests = a.fusionObjects(objects=[amesh1, multitex_crests], method='FusionTexSurfMethod')

    # addObjects into corresponding windows for captures
    mesh_with_cs.addObjects([amesh1, cs])
    cs_rois.addObjects([fusion_rois])
    cs_landmarks.addObjects([fusion_crests, a_pp_pre_sphere, a_pp_post_sphere, cs])

    raw_tractogram.addObjects([raw_tractogram])
    filtered_tractogram.addObjects([filt_tractogram])
    association_fibers.addObjects([association_streamlines, amesh2])
    u_fibers.addObjects([u_fibers, pre_line, post_line, a_pp_pre_sphere, a_pp_post_sphere])
