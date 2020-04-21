#!/bin/bash

source

dwi=$1
bvecs=$2
bvals=$3
mask=$4
dir_response=$5
dir_fod=$6
default_mrtrix_bin=${MRTRIX}
mrtrix_bin=${7-${default_mrtrix_bin}}

#estimated multi-shell multi tissues responses 
wm="${dir_response}/wm_response.txt"
gm="${dir_response}/gm_response.txt"
csf="${dir_response}/csf_response.txt"
#corresponding fod
wm_FOD="${dir_fod}/wm_fod.nii.gz"
gm_FOD="${dir_fod}/gm_fod.nii.gz"
csf_FOD="${dir_fod}/csf_fod.nii.gz"
${mrtrix_bin}/dwi2fod msmt_csd $dwi -fslgrad ${bvecs} ${bvals} -mask ${mask} ${wm} ${wm_FOD} ${gm} ${gm_FOD} ${csf} ${csf_FOD} -force

