#!/bin/bash


source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh

mr_cmd="${MRTRIX}/sh2peaks"
sequence='peaks'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}

#3 main orientations of diffusion
nb_peaks=3
#

for subj in $(cat ${SUBJ_LIST})
do
    echo ${subj}
    peaks="${BV_DB}/${subj}/${DWI}/${DWI_ACQ}/${DWI_PROC}/csd/MSMT/brain_fit/peaks.nii.gz"
    sh_coeffs="${BV_DB}/${subj}/${DWI}/${DWI_ACQ}/${DWI_PROC}/csd/MSMT/brain_fit/wm_fod.nii.gz"
    if [ ! -e "${peaks}" ] && [ -e "${sh_coeffs}" ]; then
        #optional parameters
        dir_FS_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
        mask="${dir_FS_subj_in}/nodif_brain_mask.nii.gz"
        cmd="${mr_cmd} ${sh_coeffs} ${peaks} -num ${nb_peaks} -mask ${mask}"
        ${cmd}
        launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
    fi
done



