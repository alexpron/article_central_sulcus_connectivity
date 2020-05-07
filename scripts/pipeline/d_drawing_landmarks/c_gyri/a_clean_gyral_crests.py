import os
import numpy as np
from soma import aims
from configuration import DIR_DRAWN, DIR_IN, DIR_OUT, SUBJ_LIST, SIDES, GYRI
from lines import clean_line, normalized_curv_parametrisation
from meshes_.processing import vertices_to_2d_line


if __name__ == '__main__':

    SUBJ_LIST = ['118730']
    SIDES = ['R']

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            path_mesh = os.path.join(DIR_IN, subject + '_' + side + 'white.gii')
            mesh = aims.read(path_mesh)
            vertices = np.array(mesh.vertex())
            for k, gyrus in enumerate(GYRI):

                path_gyrus = os.path.join(DIR_DRAWN, 'gyri', subject + '_' + side + '_' + gyrus + '_' + 'drawn.tex.gii')
                path_cleaned_gyrus = os.path.join(DIR_OUT, 'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                  'cleaned.npy')
                path_cleaned_gyrus_tex = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                  'cleaned.gii')
                path_cleaned_gyrus_mesh = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                  'cleaned.mesh')
                path_cleaned_gyrus_iso_param = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                  'cleaned_iso_param.npy')
                path_cleaned_gyrus_iso_param_tex = os.path.join(DIR_OUT,'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                  'cleaned_iso_param.gii')

                gyrus_tex = aims.read(path_gyrus)
                gyrus_a = np.array(gyrus_tex[0])
                #removing additionnal triangles to obtain a real line
                cleaned_gyrus = clean_line(mesh,gyrus_a)
                np.save(path_cleaned_gyrus, cleaned_gyrus)
                #saving also the cleaned gyrus as a texture for displays
                cleaned_gyrus_t = np.zeros(vertices.shape[0])
                cleaned_gyrus_t[cleaned_gyrus] = 100
                cleaned_gyrus_tex = aims.TimeTexture(cleaned_gyrus_t.astype(np.float32))
                aims.write(cleaned_gyrus_tex,path_cleaned_gyrus_tex)
                #creating a gyral line mesh
                gyrus_vertices = vertices[cleaned_gyrus]
                gyrus_mesh = vertices_to_2d_line(gyrus_vertices)
                aims.write(gyrus_mesh, path_cleaned_gyrus_mesh)
                #computing normalized curv absciss param
                gyrus_param = normalized_curv_parametrisation(gyrus_vertices)
                np.save(path_cleaned_gyrus_iso_param, gyrus_param)
                #save it also as a texture
                gyrus_param_tex = aims.TimeTexture(gyrus_param.astype(np.float32))
                aims.write(gyrus_param_tex, path_cleaned_gyrus_iso_param_tex)
