#!/bin/bash

source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

sequence='msmt_csd'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}



for subj in $(cat ${SUBJ_LIST})
do
    echo "Processing HCP subject: ${subj}\n"

    #data related files
    dir_FS_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
    dir_BV_subj_in="${BV_DB}/${subj}/dmri/default_acquisition/HCP_pipeline"
    dir_subj_in="${dir_BV_subj_in}/csd/MSMT"
    dir_subj_out="${dir_subj_in}/brain_fit"
   
    create_dir ${dir_subj_out}
    
    dwi="${dir_BV_subj_in}/corrected_dwi_${subj}.nii.gz"
    mask="${dir_FS_subj_in}/nodif_brain_mask.nii.gz"
    bvals="${dir_FS_subj_in}/bvals"
    bvecs="${dir_FS_subj_in}/bvecs"
    tissues="${dir_BV_subj_in}/5tt.mif"

    cmd="/hpc/meca/users/pron.a/HCP/scripts/DWI_processing/cmds/msmt_csd.sh  ${dwi} ${bvecs} ${bvals} ${mask} ${dir_subj_in} ${dir_subj_out}"
    echo ${cmd}
    #command on passive
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done





 
