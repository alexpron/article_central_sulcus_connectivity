#!/bin/bash
#renew arguments for the sake of clarity
subject=$1
echo ${subject}
#to have access to all the variables
source /hpc/meca/users/pron.a/HCP/scripts/set_env.sh

expert_file="${DIR_SCRIPTS}/t1_processing/FreeSurfer/expert_file"
dir_subject="${HCP_DATASET}/${subject}/T1w"
#Getting data coming out of PreFeeSurfer HCP pipeline
T1="${dir_subject}/T1w_acpc_dc_restore.nii.gz"
T2="${dir_subject}/T2w_acpc_dc_restore.nii.gz"
T1_brain="${dir_subject}/T1w_acpc_dc_restore_brain.nii.gz"
T2_brain="${dir_subject}/T2w_acpc_dc_restore_brain.nii.gz"
echo ${DIR_SCRIPTS}
echo ${FS_DB}
echo ${T1}
echo ${T2}
echo ${T1_brain}
echo ${expert_file}
#launching subject computation
${DIR_SCRIPTS}/t1_processing/FreeSurfer/FreeSurfer_hires.sh ${FS_DB} ${subject} ${T1} ${T2} ${T1_brain} ${expert_file}
