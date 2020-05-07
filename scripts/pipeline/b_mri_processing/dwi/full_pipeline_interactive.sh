#!/bin/bash

######################################################################
# Launch DWI processing pipeline for a given list of subjects  that
# respect the data structure of the script
#
# param $1: a txt file containing the subjects ids
#--------------------------------------------------------------------#

# "hard sourcing" this is bad but fast !
source ../../../../configuration/set_env.sh
source ../../../../libs/tools/tools.sh
######################################################################
SUBJ_LIST=$1

for subj in $(cat ${SUBJ_LIST})
do
    echo ${subj}
    dir_dataset_subj="${HCP_DATASET}/${subj}/T1w/Diffusion"
    #put files directly into the Brainvisa db to avoid loss of storage
    dir_BV_subj="${BV_DB}/${subj}/dmri/default_acquisition/HCP_pipeline"
    echo ${dir_BV_subj}
    create_dir  ${dir_BV_subj}
#    #Base
    dwi="${dir_dataset_subj}/data.nii.gz"
    bvals="${dir_dataset_subj}/bvals"
    bvecs="${dir_dataset_subj}/bvecs"
    dwi_corr="${dir_BV_subj}/corrected_dwi_${subj}.nii.gz"
    mask="${dir_dataset_subj}/nodif_brain_mask.nii.gz"
    #MBO
    mb0="${dir_BV_subj}/b0_${subj}.nii.gz"
    #DTI
    dir_dti="${dir_BV_subj}/dti/Mrtrix"
    dir_brain_fit="${dir_dti}/brain_fit"
    dir_derived_quantities="${dir_brain_fit}/derived_indices"
    create_dir  ${dir_derived_quantities}
    tensor="${dir_brain_fit}/${subj}_tensor_coefficients.nii.gz"
    #derived quantities
    FA="${dir_derived_quantities}/${subj}_fractionnal_anisotropy.nii.gz"
    MD="${dir_derived_quantities}/${subj}_mean_diffusivity.nii.gz"
    e1="${dir_derived_quantities}/${subj}_first_eigen_vector.nii.gz"
    #MSMT csd
    dir_csd="${dir_BV_subj}/csd/MSMT"
    dir_brain_fit_csd="${dir_csd}/brain_fit"
    create_dir  ${dir_csd}
    create_dir  ${dir_brain_fit_csd}
    tissues="${dir_BV_subj}/5tt.mif"
    #B1 bias correction
    b1biascorr="${DIR_SCRIPTS}/dwi_processing/cmds/B1_bias_correction.sh  ${dwi} ${bvals} ${bvecs} ${dwi_corr}"
    ${b1biascorr}
    #Mean BO estimation 
    meanb0="${DIR_SCRIPTS}/dwi_processing/cmds/mean_b0_extraction.sh  ${dwi_corr} ${bvecs} ${bvals} ${mb0}"
    ${meanb0}
    #Tensor Fitting 
    dtifit="${DIR_SCRIPTS}/dwi_processing/cmds/tensor.sh  ${dwi_corr} ${bvals} ${bvecs} ${mask} ${tensor} ${FA} ${MD} ${e1}"
    ${dtifit}
    #Impulsionnal Response
    imp="${DIR_SCRIPTS}/dwi_processing/cmds/impulsionnal_response_estimation.sh  ${dwi_corr} ${bvecs} ${bvals} ${tissues} ${mask} ${dir_csd}"
    ${imp}
    #MSMT deconv
    csd="${DIR_SCRIPTS}/dwi_processing/cmds/msmt_csd.sh  ${dwi_corr} ${bvecs} ${bvals} ${mask} ${dir_csd} ${dir_brain_fit_csd}"
    ${csd}
    #Peaks
done
