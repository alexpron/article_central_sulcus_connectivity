"""
Global variables and data structure used in the study
You MUST change these variable values to adapt to your own data organization
TODO: move the content of this file and of the set_env.sh file to an unique .json file to avoid redundancy
"""

import os
import numpy as np
from libs.tools.usual import merge_dicts


def read_subjects_list(path_list):
    """
    :param path_list: the path containing the IDs of the subjects
    :return: list of the subjects IDs as strings (easier for path completion)
    """
    subs = np.loadtxt(path_list)
    subjects_list = [str(int(s)) for s in subs]
    return subjects_list


#default brainvisa and associated python version used for analyses/visualisation in the paper
BRAINVISA = '/hpc/meca/users/pron.a/softs/brainvisa-4.6.1'
BRAINVISA_PYTHON = os.path.join(BRAINVISA, 'bin', 'python')

#storage directory of the preprocessed HCP S900 release dataset
HCP_DATASET = '/envau/work/meca/data/HCP/data/HCP_dataset'

#Data (output directory outside of BrainVISA database)
DATA = '/hpc/meca/users/pron.a/data'
DIR_SUBJECTS = os.path.join(DATA, 'subjects')
DIR_MESHES = os.path.join(DATA, 'meshes_and_textures')

#Subjects selection related variables
RELEASE = '07_30_2018_S900_release'
RESTRICTED = os.path.join(DIR_SUBJECTS, 'RESTRICTED' + '_' + RELEASE + '.csv')
UNRESTRICTED = os.path.join(DIR_SUBJECTS, 'unrestricted' + '_' + RELEASE + '.csv')
FULL = os.path.join(DIR_SUBJECTS, 'full' + '_' + RELEASE + '.csv')
#subjects whithout any quality check issue according to HCP report
CLEAN = os.path.join(DIR_SUBJECTS, 'clean_subjects' + '_' + RELEASE + '.csv')
# all subjects that respect our inclusion criteria
POTENTIALS = os.path.join(DIR_SUBJECTS, 'potential_subjects' + '_' + RELEASE + '.csv')
SELECTED = os.path.join(DIR_SUBJECTS, 'selected_subjects' + '_' + RELEASE + '.csv')
# selected subject list is included in this git repo for the sake of completness
PATH_SUBJ_LIST = os.path.join(os.getcwd(), 'subjects_list.txt')
SUBJ_LIST = read_subjects_list(PATH_SUBJ_LIST)

SIDES = {'L': 'Left', 'R': 'Right'}
SULCUS = 'CS' #this study focus on the central sulcus but generic organisation
GYRI = ['precentral', 'postcentral']
#Adjacent gyri of the central sulcus
ADJACENT_GYRI = {SULCUS: GYRI}
DIR_SULCUS = os.path.join(DATA, 'sulci', SULCUS)
DIR_LANDMARKS = os.path.join(DIR_SULCUS, 'landmarks')


#BrainVISA database structure and associated variables
BRAINVISA_DB = '/hpc/meca/data/U_Fibers/BV_database'
CENTER = 'subjects'
DWI = 'dmri'
T1 = 't1mri'
#acquisitions
STRUCT_ACQ = 'HCP_pipeline_modified'
DWI_ACQ = 'default_acquisition'
STRUCT_PROC = 'default_analysis'
DWI_PROC = 'HCP_pipeline'
#model instances:
CSD_MODEL = 'MSMT'
DTI_MODEL = 'Mrtrix'
FIT_INSTANCE = 'brain_fit'


BVALS = {subject: os.path.join(HCP_DATASET, subject, 'T1w', 'Diffusion', 'bvals') for subject in SUBJ_LIST}
BVECS = {subject: os.path.join(HCP_DATASET, subject, 'T1w', 'Diffusion', 'bvecs') for subject in SUBJ_LIST}
DWI_HCP = {subject: os.path.join(HCP_DATASET, subject, 'T1w', 'Diffusion','data.nii.gz') for subject in SUBJ_LIST}
DIR_T1 = {subject: os.path.join(BRAINVISA_DB, CENTER, subject, T1) for subject in SUBJ_LIST}
DIR_DWI = {subject: os.path.join(BRAINVISA_DB, CENTER, subject, DWI, DWI_ACQ, DWI_PROC) for subject in SUBJ_LIST}
COMMIT_META = {subject: os.path.join(DIR_DWI[subject], 'commit_metada.txt') for subject in SUBJ_LIST}
T1_2_DWI = {subject: os.path.join(DIR_DWI[subject], 'registration', 'T1_TO_dwi' + '_' + subject + '.trm') for subject in SUBJ_LIST}
DWI_2_T1 = {subject: os.path.join(DIR_DWI[subject], 'registration', 'dwi_TO_T1' + '_' + subject + '.trm') for subject in SUBJ_LIST}

MESHES_TYPE = ['white', 'hemi']
MESHES_BRAINVISA_T1 = {(subject, side, mesh_type, 't1'): os.path.join(DIR_T1[subject], STRUCT_ACQ, STRUCT_PROC,'segmentation','meshes', subject + '_' + side + mesh_type + '.gii') for subject in SUBJ_LIST for side in SIDES for mesh_type in MESHES_TYPE}
MESHES_BRAINVISA_DWI = {(subject, side, mesh_type, 'dwi'): os.path.join(DIR_DWI[subject],'mesh', subject + '_' + side + '_' + mesh_type + '_' + 'to_dwi.gii') for subject in SUBJ_LIST for side in SIDES for mesh_type in MESHES_TYPE}
MESHES_BRAINVISA = merge_dicts(MESHES_BRAINVISA_T1, MESHES_BRAINVISA_DWI)

MESHES = {(subject, side, mesh_type): os.path.join(DIR_MESHES, subject + '_' + side + '_' + mesh_type + '.gii') for subject in SUBJ_LIST for side in SIDES.keys() for mesh_type in MESHES_TYPE}
DEPTHS = {(subject, side, 'white'): os.path.join(DIR_MESHES, subject + '_' + side + '_' + 'white_depth.gii') for subject in SUBJ_LIST for side in SIDES.keys()}
DPFS = {(subject, side, 'white'): os.path.join(DIR_MESHES, subject + '_' + side + '_' + 'white_dpf.gii') for subject in SUBJ_LIST for side in SIDES.keys()}
CURVATURES = {(subject, side, 'white'): os.path.join(DIR_MESHES, subject + '_' + side + '_' + 'white_curvature.gii') for subject in SUBJ_LIST for side in SIDES.keys()}

STATUS = ['drawn', 'cleaned']
EXTENSIONS = {'array': '.npy', 'mesh': '.mesh', 'texture': '.gii'} #valid only for lines (fundus or crests)
EXTREMITIES = {(subject, side): os.path.join(DIR_LANDMARKS, 'extremities', subject + '_' + side + '_' + SULCUS + '_' + 'extremities'
                                                                                                        '.gii') for
               subject in SUBJ_LIST for side in SIDES.keys()}

GYRAL_CRESTS = {(subject, side, gyrus, status, nature): os.path.join(DIR_LANDMARKS,'adjacent_gyri', subject + '_' + side + '_' + gyrus + '_' + status + EXTENSIONS[nature]) for subject in SUBJ_LIST for side in SIDES.keys() for gyrus in ADJACENT_GYRI[SULCUS] for status in STATUS for nature in EXTENSIONS}
SULCUS_FUNDI = {(subject, side, SULCUS, status, nature): os.path.join(DIR_LANDMARKS,'fundi', subject + '_' + side + '_' + SULCUS + '_' + status + EXTENSIONS[nature]) for subject in SUBJ_LIST for side in SIDES.keys() for gyrus in ADJACENT_GYRI[SULCUS] for status in STATUS for nature in EXTENSIONS}
LINES = merge_dicts(GYRAL_CRESTS, SULCUS_FUNDI)

PARAMETRISATIONS = ['iso', 'global_mean','mean_by_hemi']

GYRAL_PARAMETRISATIONS = {(subject, side, gyrus, status, nature, param): os.path.join(DIR_LANDMARKS,'adjacent_gyri', subject + '_' + side + '_' + gyrus + '_' + status + '_' + param + '_param' + EXTENSIONS[nature]) for subject in SUBJ_LIST for side in SIDES.keys() for gyrus in ADJACENT_GYRI[SULCUS] for status in STATUS for nature in EXTENSIONS for param in PARAMETRISATIONS}
FUNDI_PARAMETRISATIONS = {(subject, side, SULCUS, status, nature, param): os.path.join(DIR_LANDMARKS,'fundi', subject + '_' + side + '_' + gyrus + '_' + status + '_' + param + '_param' + EXTENSIONS[nature]) for subject in SUBJ_LIST for side in SIDES.keys() for gyrus in ADJACENT_GYRI[SULCUS] for status in STATUS for nature in EXTENSIONS for param in PARAMETRISATIONS}
LINE_PARAMETRISATIONS = merge_dicts(GYRAL_PARAMETRISATIONS, FUNDI_PARAMETRISATIONS)

TABLES = ['draw_attribution', 'mesh_index', 'cs_coord', 'gyri_index', 'gyri_coord','final']
PPFM_TABLES = {t: os.path.join(DIR_LANDMARKS, 'ppfm','ppfm' + '_' + t + '.csv') for t in TABLES}

