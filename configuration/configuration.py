"""
Global variables and data structure used in the study
You MUST change these variable values to adapt to your own data organization
TODO: move the content of this file and of the set_env.sh file to an unique .json file to avoid redundancy
"""

import os
from libs.tools.usual import merge_dicts, read_subjects_list

# --------------------------------- Global Variables for the study ----------------------------------------------------#

RELEASE = "07_30_2018_S900_release"  # version of the HCP metadata used
SIDES = {"L": "Left", "R": "Right"}  # hemispheres
SULCUS = 'cs'  # this study focus on the central sulcus but generic organisation
GYRI = ["precentral", "postcentral"]
ADJACENT_GYRI = {SULCUS: GYRI}
MESHES_TYPE = ["white", "hemi"]  # white and pial triangular meshes
PARAMETRISATIONS = [
    "iso",
    "global_mean",
    "mean_by_hemi",
]  # parametrisations for the landmark lines (CS and gyri)
STATUS = ["drawn", "cleaned"]
EXTENSIONS = {
    "array": ".npy",
    "mesh": ".mesh",
    "texture": ".gii",
}  # valid only for lines (fundus or crests)
TABLES = [
    "draw_attribution",
    "mesh_index",
    "cs_coord",
    "index_gyri",
    "gyri_coord",
    "final",
]  # tables related to PPFM
TRACTS_EXTREMITIES = ["s", "e"]
DENSITIES_RADIUS = (
    5  # variance of the gaussian kernel used to provide continuous information
)
GROUP_DENSITIES_MAX = 8000

# --------------------------------- BrainVISA instance and associated python used in this study -----------------------#

BRAINVISA = "/hpc/soft/brainvisa/brainvisa_4.6.0"
BRAINVISA_PYTHON = os.path.join(BRAINVISA, "bin", "python")

# ---------------------------------- Project structure ----------------------------------------------------------------#
# TO DO : find a way to remove the absolute path inside the script directories
DIR_PROJECT = "/hpc/meca/users/pron.a/code/article"
# selected subject list is included in this git repo for the sake of completness
PATH_SUBJ_LIST = os.path.join(DIR_PROJECT, "configuration", "subjects_list.txt")
SUBJ_LIST = read_subjects_list(PATH_SUBJ_LIST)

# --------------------------------- INT storage location of the preprocessed HCP S900 release dataset -----------------#

HCP_DATASET = "/envau/work/meca/data/HCP/data/HCP_dataset"
BVALS = {
    subject: os.path.join(HCP_DATASET, subject, "T1w", "Diffusion", "bvals")
    for subject in SUBJ_LIST
}
BVECS = {
    subject: os.path.join(HCP_DATASET, subject, "T1w", "Diffusion", "bvecs")
    for subject in SUBJ_LIST
}
DWI_HCP = {
    subject: os.path.join(HCP_DATASET, subject, "T1w", "Diffusion", "data.nii.gz")
    for subject in SUBJ_LIST
}

# --------------------------------- FreeSurfer 6.0.0 database structure and associated variables ----------------------#

FS_DB = "/hpc/meca/data/U_Fibers/FS_database"
ASEGS = {
    subject: os.path.join(FS_DB, subject, "stats", "aseg.stats")
    for subject in SUBJ_LIST
}

# --------------------------------- BrainVISA database structure and associated variables -----------------------------|

BRAINVISA_DB = "/hpc/meca/data/U_Fibers/BV_database"
CENTER = "subjects"
DWI = "dmri"
T1 = "t1mri"
# acquisitions
STRUCT_ACQ = "HCP_pipeline_modified"
DWI_ACQ = "default_acquisition"
STRUCT_PROC = "default_analysis"
DWI_PROC = "HCP_pipeline"
# model instances:
CSD_MODEL = "MSMT"
DTI_MODEL = "Mrtrix"
FIT_INSTANCE = "brain_fit"

DIR_SUBJECT_BRAINVISA = {
    subject: os.path.join(BRAINVISA_DB, CENTER, subject) for subject in SUBJ_LIST
}
DIR_T1 = {
    subject: os.path.join(DIR_SUBJECT_BRAINVISA[subject], T1) for subject in SUBJ_LIST
}
DIR_DWI = {
    subject: os.path.join(DIR_SUBJECT_BRAINVISA[subject], DWI, DWI_ACQ, DWI_PROC)
    for subject in SUBJ_LIST
}
TISSUE_MASKS = {
    (subject, side): os.path.join(
        DIR_T1[subject],
        STRUCT_ACQ,
        STRUCT_PROC,
        "segmentation",
        side + "grey_white" + "_" + subject + ".nii.gz",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}
MESHES_BRAINVISA_T1 = {
    (subject, side, mesh_type, "t1"): os.path.join(
        DIR_T1[subject],
        STRUCT_ACQ,
        STRUCT_PROC,
        "segmentation",
        "meshes",
        subject + "_" + side + mesh_type + ".gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES
    for mesh_type in MESHES_TYPE
}
MESHES_BRAINVISA_DWI = {
    (subject, side, mesh_type, "dwi"): os.path.join(
        DIR_DWI[subject],
        "mesh",
        subject + "_" + side + "_" + mesh_type + "_" + "to_dwi.gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES
    for mesh_type in MESHES_TYPE
}
MESHES_BRAINVISA = merge_dicts(MESHES_BRAINVISA_T1, MESHES_BRAINVISA_DWI)
FODS = {
    subject: os.path.join(
        DIR_DWI[subject], "csd", CSD_MODEL, FIT_INSTANCE, "wm_fod.nii"
    )
    for subject in SUBJ_LIST
}
AIMS_TO_RAS = {
    subject: os.path.join(
        DIR_DWI[subject], "csd", CSD_MODEL, FIT_INSTANCE, "wm_fod_ras_to_aims.npy"
    )
    for subject in SUBJ_LIST
}
COMMIT_DIR = {
    subject: os.path.join(DIR_DWI[subject], "commit") for subject in SUBJ_LIST
}
COMMIT_META = {
    subject: os.path.join(DIR_DWI[subject], "commit_metada.txt")
    for subject in SUBJ_LIST
}
COMMIT_WEIGHTS = {
    subject: os.path.join(COMMIT_DIR[subject], "Results_StickZeppelinBall")
    for subject in SUBJ_LIST
}
T1_2_DWI = {
    subject: os.path.join(
        DIR_DWI[subject], "registration", "T1_TO_dwi" + "_" + subject + ".trm"
    )
    for subject in SUBJ_LIST
}
DWI_2_T1 = {
    subject: os.path.join(
        DIR_DWI[subject], "registration", "dwi_TO_T1" + "_" + subject + ".trm"
    )
    for subject in SUBJ_LIST
}
TTVIS = {
    subject: os.path.join(DIR_DWI[subject], "5ttvisu.nii.gz") for subject in SUBJ_LIST
}
SEED_MASK = {
    subject: os.path.join(DIR_DWI[subject], "seeding_mask.nii.gz")
    for subject in SUBJ_LIST
}
PEAKS = {
    subject: os.path.join(
        DIR_DWI[subject], "csd", CSD_MODEL, FIT_INSTANCE, "peaks.nii.gz"
    )
    for subject in SUBJ_LIST
}
TRACTS = {
    (subject, tract_type, status): os.path.join(
        DIR_DWI[subject], "tractography", subject + "track." + tract_type
    )
    for subject in SUBJ_LIST
    for tract_type in ["tck", "trk"]
    for status in ["", "filtered"]
}

FIEDLER_TABLES = {
    side: os.path.join(
        BRAINVISA_DB, "group" + "_" + side + "_" + "average_Fiedler_length.csv"
    )
    for side in SIDES.keys()
}
AREA_TABLES = {
    side: os.path.join(
        BRAINVISA_DB, "group" + "_" + side + "_" + "average_Fiedler_length.csv"
    )
    for side in SIDES.keys()
}
# ----------------------- Data (output directory outside of BrainVISA database)

DATA = "/hpc/meca/users/pron.a/data/u_fibers_test"
DIR_CLUSTER = "/hpc/meca/users/pron.a/cluster"  # Only useful in the INT context
DIR_SUBJECTS = os.path.join(DATA, "subjects")
DIR_MESHES = os.path.join(DATA, "meshes_and_textures")
DIR_SULCUS = os.path.join(DATA, "sulci", SULCUS)
DIR_LANDMARKS = os.path.join(DIR_SULCUS, "landmarks")
DIR_CONNECTIVITY = os.path.join(DIR_SULCUS, 'connectivity_space')
DIR_STATS = os.path.join(DIR_SULCUS, "statistics")
DIR_FIGURES = os.path.join(DIR_SULCUS, "figures")


# Subjects selection related variables
RESTRICTED = os.path.join(DIR_SUBJECTS, "RESTRICTED" + "_" + RELEASE + ".csv")
UNRESTRICTED = os.path.join(DIR_SUBJECTS, "unrestricted" + "_" + RELEASE + ".csv")
FULL = os.path.join(DIR_SUBJECTS, "full" + "_" + RELEASE + ".csv")
# subjects whithout any quality check issue according to HCP report
CLEAN = os.path.join(DIR_SUBJECTS, "clean_subjects" + "_" + RELEASE + ".csv")
# all subjects that respect our inclusion criteria
POTENTIALS = os.path.join(DIR_SUBJECTS, "potential_subjects" + "_" + RELEASE + ".csv")
SELECTED = os.path.join(DIR_SUBJECTS, "selected_subjects" + "_" + RELEASE + ".csv")

# Meshes and textures (landmarks extraction)
MESHES = {
    (subject, side, mesh_type): os.path.join(
        DIR_MESHES, subject + "_" + side + "_" + mesh_type + ".gii"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for mesh_type in MESHES_TYPE
}

DEPTHS = {
    (subject, side, "white"): os.path.join(
        DIR_MESHES, subject + "_" + side + "_" + "white_depth.gii"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}

DPFS = {
    (subject, side, "white"): os.path.join(
        DIR_MESHES, subject + "_" + side + "_" + "white_dpf.gii"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}

CURVATURES = {
    (subject, side, "white"): os.path.join(
        DIR_MESHES, subject + "_" + side + "_" + "white_curvature.gii"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}

EXTREMITIES = {
    (subject, side): os.path.join(
        DIR_LANDMARKS,
        "extremities",
        subject + "_" + side + "_" + SULCUS + "_" + "extremities" + ".gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}

GYRAL_CRESTS = {
    (subject, side, gyrus, status, nature): os.path.join(
        DIR_LANDMARKS,
        "adjacent_gyri",
        status,
        subject + "_" + side + "_" + gyrus + "_" + status + EXTENSIONS[nature],
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for gyrus in ADJACENT_GYRI[SULCUS]
    for status in STATUS
    for nature in EXTENSIONS
}

SULCUS_FUNDI = {
    (subject, side, SULCUS, status, nature): os.path.join(
        DIR_LANDMARKS,
        "fundus",
        status,
        subject + "_" + side + "_" + SULCUS + EXTENSIONS[nature],
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for status in STATUS
    for nature in EXTENSIONS
}

LINES = merge_dicts(GYRAL_CRESTS, SULCUS_FUNDI)

# Line parametrisation
GYRAL_PARAMETRISATIONS = {
    (subject, side, gyrus, status, nature, param): os.path.join(
        DIR_LANDMARKS,
        "adjacent_gyri",
        status,
        subject
        + "_"
        + side
        + "_"
        + gyrus
        + "_"
        + status
        + "_"
        + param
        + "_param"
        + EXTENSIONS[nature],
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for gyrus in ADJACENT_GYRI[SULCUS]
    for status in STATUS
    for nature in EXTENSIONS
    for param in PARAMETRISATIONS
}

FUNDI_PARAMETRISATIONS = {
    (subject, side, SULCUS, status, nature, param): os.path.join(
        DIR_LANDMARKS,
        "fundi",
        subject
        + "_"
        + side
        + "_"
        + SULCUS
        + "_"
        + status
        + "_"
        + param
        + "_param"
        + EXTENSIONS[nature],
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for gyrus in ADJACENT_GYRI[SULCUS]
    for status in STATUS
    for nature in EXTENSIONS
    for param in PARAMETRISATIONS
}

LINE_PARAMETRISATIONS = merge_dicts(GYRAL_PARAMETRISATIONS, FUNDI_PARAMETRISATIONS)

GEO_DISTS = {
    (subject, side, "white", gyrus): os.path.join(
        DIR_LANDMARKS,
        "surf_rois",
        "geodesic_distances",
        subject + "_" + side + "_" + gyrus + "_" + "geodesic_distance_map.gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for gyrus in ADJACENT_GYRI[SULCUS]
}
ROI_DISTANCES = {
    (subject, side, gyrus): os.path.join(
        DIR_LANDMARKS,
        "surf_rois",
        "adaptive_threshold",
        subject
        + "_"
        + side
        + "_"
        + gyrus
        + "_"
        + "dist_threshold"
        + ".npy",
    )
    for subject in SUBJ_LIST
    for side in SIDES
    for gyrus in ADJACENT_GYRI[SULCUS]
}

PARTITIONS = {
    (subject, side, gyrus): os.path.join(
        DIR_LANDMARKS,
        "surf_rois",
        "partitions",
        subject + "_" + side + "_" + gyrus + "_" + "partition" + ".gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES
    for gyrus in ADJACENT_GYRI[SULCUS]
}

ADJ_GYRI_ROI = {
    (subject, side, gyrus): os.path.join(
        DIR_LANDMARKS,
        "surf_rois",
        "rois",
        subject + "_" + side + "_" + gyrus + "_" + "surface_roi" + ".gii",
    )
    for subject in SUBJ_LIST
    for side in SIDES
    for gyrus in ADJACENT_GYRI[SULCUS]
}

PPFM_TABLES = {
    t: os.path.join(DIR_LANDMARKS, "ppfm", "tables", "ppfm" + "_" + t + ".csv")
    for t in TABLES
}

TRACTOGRAMS = {
    subject: os.path.join(DATA, "streamlines", "tractograms", subject + '.npy')
    for subject in SUBJ_LIST
}

ASSOCIATION_TRACTS = {
    (subject, side): os.path.join(
        DATA, "streamlines", "association_tracts", subject + "_" + side + ".npy"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}
STREAM_EXTREMITIES = {
    (subject, side, ext): os.path.join(
        DATA,
        "streamlines",
        "extremities",
        subject + "_" + side + "_" + ext + '_' + 'points' + ".npy",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for ext in TRACTS_EXTREMITIES
}
NEAREST_VERTEX = {
    (subject, side, ext): os.path.join(
        DATA,
        "streamlines",
        "nearest_mesh_vertex",
        subject + "_" + side + "_" + ext + "_" + "nearest_vertex.npy",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for ext in TRACTS_EXTREMITIES
}

U_FIBERS_MASK = {
    (subject, side): os.path.join(
        DATA, "u-fibers", subject + "_" + side + "_" + "mask" + ".npy"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}

# Connectivity space
U_FIBERS_INDEXES = os.path.join(
    DIR_SULCUS,  "connectivity_space", 'indexes', "u_fibers_indexes_on_gyri.npy"
)
HEMI_INDEXES = os.path.join(DIR_SULCUS, "connectivity_space", 'indexes', "hemispheres_indexes.npy")
HEMI_INDEXES_FILT = os.path.join(
    DIR_SULCUS, "connectivity_space", 'indexes', "hemispheres_index_filtered.npy"
)

U_FIBERS_COORD = {
    p: os.path.join(
        DATA,
        "sulci",
        "CS",
        "connectivity",
        "coordinates",
        "length_filtered",
        "U_fibers_coord" + "_" + p + ".npy",
    )
    for p in PARAMETRISATIONS
}
X_GRID = os.path.join(DATA, "connectivity_space", "X.npy")
Y_GRID = os.path.join(DATA, "connectivity_space", "Y.npy")
U_FIBERS_GROUP_PROFILES = {
    (side, p): os.path.join(
        DATA,
        "sulci",
        "CS",
        "connectivity",
        "profiles",
        "group",
        side + "_" + p + ".npy",
    )
    for side in SIDES.keys()
    for p in PARAMETRISATIONS
}
U_FIBERS_INDIV_PROFILES = {
    (subject, side, p): os.path.join(
        DATA,
        "sulci",
        "CS",
        "connectivity",
        "profiles",
        "subjects",
        p + "_" + subject + "_" + side + "_" + "filtered_radius_5" + ".npy",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for p in PARAMETRISATIONS
}

# Parameters obtained and fixed for DBSCAN clustering of group profiles
EPS = 3
ABS = 12000
NORM_THRESHOLD = ABS / 249897.0

DBSCAN_LABELS = os.path.join(
    DATA, "connectivity_space", "clustering", "dbscan_labels.npy"
)

# parameters used for Gaussian Mixture Model
N = 3
N_INIT = 1000
MAX_ITER = 5000
INIT_METHOD = "kmeans"

CLUSTERING_LABELS = {
    side: os.path.join(
        DATA, "sulci",
        "CS", "connectivity", "clustering", "labels" + "_" + side + ".npy"
    )
    for side in SIDES.keys()
}


# Statistics tables
ICV_DF = os.path.join(DIR_STATS, "init_tables", "ICV.csv")
FIEDLER_DF = os.path.join(DIR_STATS, "init_tables", "Fiedler_length.csv")
MESH_AREA_DF = os.path.join(DIR_STATS, "init_tables", "mesh_area.csv")
PPFM_DF = os.path.join(DIR_STATS, "init_tables", "ppfm.csv")

# Figures
DIR_PROFILES = os.path.join(DIR_FIGURES, "connectivity_profiles", "densities")
FIG_GROUP_PROFILES = {
    side: os.path.join(DIR_PROFILES, "group", side + "_" + "group_profile" + ".tiff")
    for side in SIDES.keys()
}
FIG_GROUP_PROFILES_MAXIMA = {
    side: os.path.join(
        DIR_PROFILES, "group", side + "_" + "group_profile_with_maxima" + ".tiff"
    )
    for side in SIDES.keys()
}
FIG_INDIV_PROFILES = {
    (subject, side, param, ppfm): os.path.join(
        DIR_PROFILES,
        "subjects",
        subject + "_" + side + "_" + param + "_" + ppfm + "_" + "ppfm" + ".tiff",
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
    for param in PARAMETRISATIONS
    for ppfm in ["group", "individual"]
}

DIR_CLUSTERS = os.path.join(DIR_FIGURES, "connectivity_profiles", "group_clustering")

FIG_CLUSTERS_INDIV_SPACE = {
    (subject, side): os.path.join(
        DIR_CLUSTERS, "subjects_space", subject + "_" + side + ".tiff"
    )
    for subject in SUBJ_LIST
    for side in SIDES.keys()
}
