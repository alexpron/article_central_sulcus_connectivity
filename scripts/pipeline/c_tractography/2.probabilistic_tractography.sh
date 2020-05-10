#!/bin/bash


source "${DIR_SCRIPTS}/tools.sh"
sequence='tractography'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}

#Tractography parameters
algo='iFOD2'
nb_tracks='5000000'
step='0.625'
angle='45'
max_length='300'
cutoff='0.1'

for subj in $(cat ${SUBJ_LIST})
do
        echo ${subj}
        processing_dir="${BV_DB}/${subj}/${DWI}/${DWI_ACQ}/${DWI_PROC}"
        seeding_dir="${processing_dir}/seeds"
        tractography_dir="${processing_dir}/tractography"
        create_dir ${seeding_dir}
        create_dir ${tractography_dir}
        tissues="${processing_dir}/5tt.mif"
        seeding_mask="${processing_dir}/seeding_mask.nii.gz"
        wm_FOD="${processing_dir}/csd/${CSD_MODEL}/${FIT_INSTANCE}/wm_fod.nii.gz"
        tracks="${tractography_dir}/${subj}_tracks.tck"
        if [ ! -e "${tracks}" ] ;then
            echo ${subj}
            cmd="${MRTRIX}/tckgen -algorithm ${algo} -select ${nb_tracks} -step ${step} -angle ${angle} -maxlength ${max_length} -cutoff ${cutoff} -seed_gmwmi ${seeding_mask} -act ${tissues}  ${wm_FOD} ${tracks} -force"
            launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
        fi
  done

