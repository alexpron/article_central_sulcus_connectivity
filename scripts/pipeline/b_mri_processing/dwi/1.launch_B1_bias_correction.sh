#!/bin/bash

#####################################################################
# Script to lauch the import of FreeSurfer HCP preprocessed subjects 
# bv_proc must have been created on a previous step
# Rem this step must be launched on the head of the INT cluster head
# (frioul)
#
#####################################################################

source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

sequence='B1_bias_correction'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}


for subj in $(cat ${SUBJ_LIST})
do
    echo ${subj}
    dir_subj_in=${HCP_DATASET}'/'${subj}'/T1w/Diffusion'
    #put files directly into the Brainvisa db to avoid loss of storage
    dir_subj_out=${BV_DB}'/'${subj}'/dmri/default_acquisition/HCP_pipeline'
    create_dir ${dir_subj_out}
    #
    dwi="${dir_subj_in}/data.nii.gz"
    bvals="${dir_subj_in}/bvals"
    bvecs="${dir_subj_in}/bvecs"
    dwi_corr="${dir_subj_out}/corrected_dwi_${subj}.nii.gz"
    #cluster related files
    cmd="${DIR_SCRIPTS}/DWI_processing/cmds/${sequence}.sh  ${dwi} ${bvals} ${bvecs}  ${dwi_corr}"
    echo ${cmd}
    #command on passive
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done
