#!/bin/bash

######################################################################
# Script to lauch tissue classification to constrain tractography 
#
# Rem this step must be launched on the head of the cluster (frioul)
#--------------------------------------------------------------------#
# Author: Alexandre Pron, contact: alexandre.pron@univ-amu.fr
######################################################################


##############################################################################################

source /hpc/meca/users/pron.a/HCP/scripts/set_env.sh

#iterate on HCP subjects
#for subj in $(cat ${SUBJ_LIST})
for subj in '144125' '346137' '196346' '598568' '147030' '432332' '129129' '285345' '571144' '156637' '583858' '132017' '189450'
do
    #files for the command
    dir_BV_subj="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}"
    mkdir -p ${dir_BV_subj}
    parcellation="${HCP_DATASET}/${subj}/T1w/aparc+aseg.nii.gz"
    tissues="${dir_BV_subj}/5tt.mif"
    tissues_visu="${dir_BV_subj}/5ttvisu.nii.gz"
    cmd1="${MRTRIX}/5ttgen -nocrop -sgm_amyg_hipp freesurfer ${parcellation}  ${tissues}"
    cmd2="${MRTRIX}/5tt2vis  ${tissues} ${tissues_visu}"
    ${cmd1} ; ${cmd2} 
done
