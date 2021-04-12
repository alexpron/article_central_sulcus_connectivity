import numpy as np
from soma import aims
from libs.lines import clean_line, normalized_curv_parametrisation
from libs.tools.aims.meshes.processing import vertices_to_2d_line
from configuration.configuration import (
    SUBJ_LIST,
    SIDES,
    GYRI,
    MESHES,
    GYRAL_CRESTS,
    GYRAL_PARAMETRISATIONS,
)

if __name__ == "__main__":

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            mesh = aims.read(MESHES[(subject, side, "white")])
            vertices = np.array(mesh.vertex())
            for k, gyrus in enumerate(GYRI):
                gyrus_tex = aims.read(
                    GYRAL_CRESTS[(subject, side, gyrus, "drawn", "texture")]
                )
                gyrus_a = np.array(gyrus_tex[0])
                # removing additionnal triangles to obtain a real line
                cleaned_gyrus = clean_line(mesh, gyrus_a)
                np.save(
                    GYRAL_CRESTS[(subject, side, gyrus, "cleaned", "array")],
                    cleaned_gyrus,
                )
                # saving also the cleaned gyrus as a texture for displays
                cleaned_gyrus_t = np.zeros(vertices.shape[0])
                cleaned_gyrus_t[cleaned_gyrus] = 100
                cleaned_gyrus_tex = aims.TimeTexture(cleaned_gyrus_t.astype(np.float32))
                aims.write(
                    cleaned_gyrus_tex,
                    GYRAL_CRESTS[(subject, side, gyrus, "cleaned", "texture")],
                )
                # creating a gyral line mesh
                gyrus_vertices = vertices[cleaned_gyrus]
                gyrus_mesh = vertices_to_2d_line(gyrus_vertices)
                aims.write(
                    gyrus_mesh, GYRAL_CRESTS[(subject, side, gyrus, "cleaned", "mesh")]
                )
                # computing normalized curv absciss param
                gyrus_param = normalized_curv_parametrisation(gyrus_vertices)
                np.save(
                    GYRAL_PARAMETRISATIONS[
                        (subject, side, gyrus, "cleaned", "array", "iso")
                    ],
                    gyrus_param,
                )
                # save it also as a texture
                gyrus_param_tex = aims.TimeTexture(gyrus_param.astype(np.float32))
                aims.write(
                    gyrus_param_tex,
                    GYRAL_PARAMETRISATIONS[
                        (subject, side, gyrus, "cleaned", "texture", "iso")
                    ],
                )
