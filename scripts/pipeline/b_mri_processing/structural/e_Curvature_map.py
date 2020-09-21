"""
Iterate curvature computation on all grey/white matter interface triangular meshes
"""
from libs.tools.brainvisa import compute_surfacic_curvature
from configuration.configuration import SUBJ_LIST, SIDES, MESHES, CURVATURES

if __name__ == "__main__":

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            compute_surfacic_curvature(
                MESHES[(subject, side, "white")], CURVATURES[(subject, side, "white")]
            )
