#!/bin/bash
source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

sequence='freesurfer_hires_processing'
dir_cluster="${DIR_CLUSTER}/${sequence}"
expert_file="${DIR_SCRIPTS}/t1_processing/FreeSurfer/expert_file"
create_dir ${dir_cluster}

for subject in $(cat ${SUBJ_LIST}):
do
    dir_subject="${HCP_DATASET}/${subject}/T1w"
    #Getting data coming out of PreFeeSurfer HCP pipeline
    T1="${dir_subject}/T1w_acpc_dc_restore.nii.gz"
    T2="${dir_subject}/T2w_acpc_dc_restore.nii.gz"
    T1_brain="${dir_subject}/T1w_acpc_dc_restore_brain.nii.gz"
    T2_brain="${dir_subject}/T2w_acpc_dc_restore_brain.nii.gz"
    #first step of the freesurfer HCP pipeline
    cmd="${DIR_SCRIPTS}/t1_processing/FreeSurfer/FreeSurfer_hires.sh ${FS_DB} ${subject} ${T1} ${T2} ${T1_brain}
    ${expert_file}"
    dir_subject_freesurfer="${FS_DB}/${subject}"
    if [ ! -d ${dir_subject_freesurfer} ]; then
        echo ${subject}
        launch_subject_cmd "${cmd}" ${subject} ${dir_cluster} 12
    else
        echo "Subject ${subject} has already been processed with freesurfer"
    fi
done
