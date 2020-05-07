#!/bin/bash


source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

sequence='impulsionnal_response_estimation'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}

for subj in $(cat ${SUBJ_LIST})
do
    echo "Processing HCP subject: ${subj}\n"
    #
    dir_dataset_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
    dir_BV_subj_in="${BV_DB}/${subj}/dmri/default_acquisition/HCP_pipeline"
    dir_subj_out="${dir_BV_subj_in}/csd/MSMT"
   
    create_dir ${dir_subj_out}
    
    dwi="${dir_BV_subj_in}/corrected_dwi_${subj}.nii.gz"
    mask="${dir_dataset_subj_in}/nodif_brain_mask.nii.gz"
    bvals="${dir_dataset_subj_in}/bvals"
    bvecs="${dir_dataset_subj_in}/bvecs"
    tissues="${dir_BV_subj_in}/5tt.mif"

    cmd="${DIR_SCRIPTS}/DWI_processing/cmds/${sequence}.sh  ${dwi} ${bvecs} ${bvals} ${tissues} ${mask} ${dir_subj_out}"
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done





 
