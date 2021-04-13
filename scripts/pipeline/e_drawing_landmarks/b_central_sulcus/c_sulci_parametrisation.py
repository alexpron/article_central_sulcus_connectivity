import numpy as np
from soma import aims
from libs.lines import normalized_curv_parametrisation
from configuration.configuration import (
    SUBJ_LIST,
    SIDES,
    MESHES,
    SULCUS_FUNDI,
    SULCUS,
    FUNDI_PARAMETRISATIONS,
)

if __name__ == "__main__":

    for subject in SUBJ_LIST:
        for side in SIDES:
            fundus_index = np.load(
                SULCUS_FUNDI[(subject, side, SULCUS, "cleaned", "array")]
            )
            mesh = aims.read(MESHES[(subject, side)])
            vertices = np.array(mesh.vertex())
            fundus = vertices[fundus_index]
            norm_param = normalized_curv_parametrisation(fundus)
            norm_param_tex = aims.TimeTexture(norm_param)
            np.save(
                FUNDI_PARAMETRISATIONS[
                    (subject, side, SULCUS, "cleaned", "array", "iso")
                ],
                norm_param,
            )
            aims.write(
                norm_param_tex,
                FUNDI_PARAMETRISATIONS[
                    (subject, side, SULCUS, "cleaned", "texture", "iso")
                ],
            )
