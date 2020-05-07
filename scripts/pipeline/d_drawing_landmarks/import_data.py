"""
This script aims at retrieving the data needed from the BrainVISA database on the INT cluster to local instance of the project
in order to manually draw surface landmarks of the central sulcus. It was created to ease drawing (faster in local, all files in the same directory).
For each subject, the extracted data are:

- the grey/white interface mesh, here called white mesh for both hemispheres (Aims mm diffusion space).
- the pial mesh here called, here called pial mesh for both hemispheres
- the Depth Potential Function (DPF) to help draw the extremities, sulcal and gyral lines.
- the Geodesic Depth for the depth profiles along the sulcal line and the PPFM extraction.

Those data are copied in the data directory associated to the Project. Subdirectories were not made to further split the data
since it is far more convenient to have all the required data (meshes and texture) to draw using SurfPaint.
"""

from __future__ import print_function
import os
import shutil
from configuration import SUBJ_LIST, SIDES, DIR_IN, BV_DB, STRUCT, DWI, STRUCT_ACQ, DWI_ACQ, STRUCT_PROC, DWI_PROC

def get_data():
    for i, subject in enumerate(SUBJ_LIST):
        dir_subject = os.path.join(BV_DB, subject)
        dir_t1 = os.path.join(dir_subject, STRUCT)
        dir_dwi = os.path.join(dir_subject, DWI )
        dir_segmentation = os.path.join(dir_t1, STRUCT_ACQ, STRUCT_PROC, 'segmentation')
        dir_surface_analysis = os.path.join(dir_segmentation,'mesh','surface_analysis')
        dir_mesh_dwi = os.path.join(dir_dwi, DWI_ACQ, DWI_PROC,'mesh')
        #meshes and textures are split into hemispheres
        for j, side in enumerate(SIDES):
                path_mesh_in = os.path.join(dir_mesh_dwi, subject + '_' + side + 'white_to_dwi.gii')
                path_DPF_in = os.path.join(dir_surface_analysis, subject + '_' + side + 'white_DPF.gii')
                path_depth_in = os.path.join(dir_segmentation, subject + '_' + side + 'white_depth.gii')
                path_mesh_out = os.path.join(DIR_IN, subject + '_' + side + 'white.gii')
                path_DPF_out = os.path.join(DIR_IN, subject + '_' + side + 'white_DPF.gii')
                path_depth_out = os.path.join(DIR_IN, subject + '_' + side + 'white_depth.gii')

                print("subject", subject, side , "Hemisphere")
                if os.path.exists(path_mesh_in):
                    shutil.copy2(path_mesh_in, path_mesh_out)
                    print("mesh copied")
                if os.path.exists(path_DPF_in):
                    shutil.copy2(path_DPF_in, path_DPF_out)
                    print("DPF copied")
                if os.path.exists(path_depth_in):
                    shutil.copy2(path_depth_in, path_depth_out)
                    print("Depth copied")





if __name__ == '__main__':

    get_data()


                        

