"""Retrieve the data needed from the BrainVISA database of the HCP project.
For each subject, the extracted data are:

- the grey/white interface mesh, here called white mesh for both hemispheres (Aims diffusion space).
- the pial mesh here called, here called hemi mesh for both hemispheres (Aims diffusion space)

Those data are copied in the data directory associated to the Project. Subdirectories were not made to further split the data
since it is far more convenient to have all the required data (meshes and texture) to draw using SurfPaint.

Note that a copy was used instead of symbolic link or direct path to ease the visualisation (local data and local Anatomist) 
and the drawing of gyral lines (Using Surfpaint with additional texture is easier if the original mesh is in the same directory)
Specific to INT configuration, do not use ! Kept for the sake of clarity and transparency
"""

from __future__ import print_function
import os
import shutil
from configuration.configuration import SUBJ_LIST, SIDES, MESHES_BRAINVISA_DWI, MESHES, MESHES_TYPE


def main():
    """
    Wrapper to extract white and hemi meshes from the BrainVISA database into local directory
    :return:
    """
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for mesh_type in MESHES_TYPE:
                if os.path.exists(MESHES_BRAINVISA_DWI[(subject, side)]):
                    shutil.copy2(MESHES_BRAINVISA_DWI[(subject, side, mesh_type)], MESHES[(subject, side, mesh_type)])
    pass


if __name__ == '__main__':
    main()
