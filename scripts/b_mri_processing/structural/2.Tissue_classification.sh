#!/bin/bash

######################################################################
# Script to lauch tissue classification to constrain tractography 
#
# Rem this step must be launched on the head of the cluster (frioul)
#--------------------------------------------------------------------#
# Author: Alexandre Pron, contact: alexandre.pron@univ-amu.fr
######################################################################

source "${DIR_SCRIPTS}/tools.sh"
##############################################################################################

#Different files according to sequences (eg import etc.)
sequence='tissue_classification'
dir_proc=${DIR_BV_PROC}'/'${sequence}
dir_cluster=${DIR_CLUSTER}'/'${sequence}
create_dir ${dir_cluster}

#iterate on HCP subjects
#for subj in $(cat ${SUBJ_LIST})
for subj in '195849'
do
    #files for the command
    dir_BV_subj="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}"
    parcellation="${HCP_DATASET}/${subj}/T1w/aparc+aseg.nii.gz"
    tissues="${dir_BV_subj}/5tt.mif"
    tissues_visu="${dir_BV_subj}/5ttvisu.nii.gz"
    cmd1="${MRTRIX}/5ttgen -nocrop -sgm_amyg_hipp freesurfer ${parcellation}  ${tissues}"
    cmd2="${MRTRIX}/5tt2vis  ${tissues} ${tissues_visu}"
    cmd="${cmd1} ; ${cmd2}"
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done
