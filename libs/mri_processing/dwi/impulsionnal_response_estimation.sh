#!/bin/bash

#estimating multi-shell multi tissues responses from FreeSurfer tissue segmentation

source ../../../../configuration/set_env.sh

dwi=$1
bvecs=$2
bvals=$3
tissues=$4
mask=$5
dir_response=$6
mrtrix_bin=${7-${MRTRIX}}

wm="${dir_response}/wm_response.txt"
gm="${dir_response}/gm_response.txt"
csf="${dir_response}/csf_response.txt"

${mrtrix_bin}/dwi2response msmt_5tt -mask ${mask} -fslgrad ${bvecs} ${bvals}  ${dwi} ${tissues} ${wm} ${gm} ${csf} 

