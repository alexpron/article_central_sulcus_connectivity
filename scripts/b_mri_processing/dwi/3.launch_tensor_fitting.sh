#!/bin/bash

source ../tools.sh
##############################################################################################
#remark: FS_db is not a FreeSurfer database it is a the copy of preprocessed data from the HCP

sequence='tensor'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}


#for subj in $(cat ${SUBJ_LIST})
for subj in '195849'
do
    echo "Processing HCP subject: ${subj}\n"
    #cluster related files
    s
    #data related files
    dir_dataset_subj_in="${HCP_DATASET}/${subj}/T1w/Diffusion"
    dir_BV_subj_in="${BV_DB}/${subj}/dmri/default_acquisition/HCP_pipeline"
    dir_subj_out="${dir_BV_subj_in}/dti/Mrtrix"
    dir_brain_fit="${dir_subj_out}/brain_fit"
    dir_derived_quantities="${dir_brain_fit}/derived_indices"
    create_dir ${dir_derived_quantities}
    #directorries are set according to Diffuse toolbox ontology
    dwi="${dir_BV_subj_in}/corrected_dwi_${subj}.nii.gz"
    mask="${dir_dataset_subj_in}/nodif_brain_mask.nii.gz"
    bvals="${dir_dataset_subj_in}/bvals"
    bvecs="${dir_dataset_subj_in}/bvecs"
    tensor="${dir_brain_fit}/${subj}_tensor_coefficients.nii.gz"
    #derived quantities
    FA="${dir_derived_quantities}/${subj}_fractionnal_anisotropy.nii.gz"
    MD="${dir_derived_quantities}/${subj}_mean_diffusivity.nii.gz"
    e1="${dir_derived_quantities}/${subj}_first_eigen_vector.nii.gz"

    cmd="${DIR_SCRIPTS}/DWI_processing/cmds/${sequence}.sh  ${dwi} ${bvals} ${bvecs} ${mask} ${tensor} ${FA} ${MD} ${e1}"
    echo ${cmd}
    #command on passive
    launch_subject_cmd "${cmd}" ${subj} ${dir_cluster}
done





 
