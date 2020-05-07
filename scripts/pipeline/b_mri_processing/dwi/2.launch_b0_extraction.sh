#!/bin/bash




source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

#Different files according to sequences (eg import etc.)
sequence='mean_b0_extraction'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}

for subj in $(cat ${SUBJ_LIST})
do
    echo "Processing HCP subject: ${subj}"
    #data related files
    dir_dataset_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
    dir_BV_subj_in="${BV_DB}/${subj}/dmri/default_acquisition/HCP_pipeline"

    dwi="${dir_BV_subj_in}/corrected_dwi_${subj}.nii.gz"
    mask="${dir_dataset_subj_in}/nodif_brain_mask.nii.gz"
    bvals="${dir_dataset_subj_in}/bvals"
    bvecs="${dir_dataset_subj_in}/bvecs"
    mb0="${dir_BV_subj_in}/b0_${subj}.nii.gz"

    cmd="${DIR_SCRIPTS}/DWI_processing/cmds/${sequence}.sh  ${dwi} ${bvecs} ${bvals} ${mb0}"
    echo ${cmd}
    #command on passive
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done





 
