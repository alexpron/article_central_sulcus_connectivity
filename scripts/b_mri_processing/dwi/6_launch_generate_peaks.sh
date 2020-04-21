#!/bin/bash
source /hpc/meca/users/pron.a/HCP/scripts/set_env.sh
source "${DIR_SCRIPTS}/tools.sh"
mr_cmd="${MRTRIX}/sh2peaks"
sequence='peaks'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}

#3 main orientations of diffusion
nb_peaks=3
#
#for subj in $(cat ${SUBJ_LIST})
for subj in '144125' '346137' '196346' '598568' '147030' '432332' '129129' '285345' '571144' '156637' '583858' '132017' '189450'
do
    echo ${subj}
    peaks="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/csd/MSMT/brain_fit/peaks.nii.gz"
    sh_coeffs="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/csd/MSMT/brain_fit/wm_fod.nii.gz"
    if [ ! -e "${peaks}" ] && [ -e "${sh_coeffs}" ]; then
        #optional parameters
        dir_FS_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
        mask="${dir_FS_subj_in}/nodif_brain_mask.nii.gz"
        cmd="${mr_cmd} ${sh_coeffs} ${peaks} -num ${nb_peaks} -mask ${mask}"
        ${cmd}
        #launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
    fi
done



