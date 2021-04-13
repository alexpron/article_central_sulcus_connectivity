from __future__ import print_function
import os
import numpy as np
from soma import aims
from libs.lines import get_sulcus_fundus_from_extremities


from configuration.configuration import (
    EXTREMITIES,
    MESHES,
    DPFS,
    SUBJ_LIST,
    SIDES,
    SULCUS_FUNDI,
)


def extract_sulcus_fundus_from_extremities(path_mesh, path_dpf, path_extremities):
    """
    Wrapper of the get_sulcus_from_extremities function
    """
    mesh = aims.read(path_mesh)
    dpf = aims.read(path_dpf)
    extremities = aims.read(path_extremities)
    ext = np.array(extremities[0])
    # round the texture to avoid error when texture modified in SurfPaint
    ext = np.round(ext)
    start = np.where(ext == 50.00)[0][0]
    end = np.where(ext == 100.00)[0][0]
    # draw sulcus fundus line and retrieve ist vertices index on mesh
    sulcus = get_sulcus_fundus_from_extremities(start, end, mesh, dpf)
    return sulcus


if __name__ == "__main__":

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in SIDES:
            path_extremities = EXTREMITIES[subject, side]
            if os.path.exists(path_extremities):
                path_mesh = MESHES[subject, side, 'white']
                path_dpf = DPFS[subject, side]
                sulcus_fundus = extract_sulcus_fundus_from_extremities(path_mesh, path_dpf, path_extremities)
                # sulcus fundus as mesh index list
                path_fundus_index = SULCUS_FUNDI[
                    subject, side, "drawn", "array"]
                np.save(path_fundus_index, sulcus_fundus)
            else:
                print(
                    "Extremities texture does not exists for subject  ",
                    subject,
                    side,
                    " Hemisphere",
                )
