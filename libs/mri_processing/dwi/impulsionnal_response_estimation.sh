#!/bin/bash


dwi=$1
bvecs=$2
bvals=$3
tissues=$4
mask=$5
dir_response=$6
default_mrtrix_bin='/hpc/meca/softs/mrtrix/bin'
mrtrix_bin=${7-${default_mrtrix_bin}}

#estimating multi-shell multi tissues responses 
wm="${dir_response}/wm_response.txt"
gm="${dir_response}/gm_response.txt"
csf="${dir_response}/csf_response.txt"
${mrtrix_bin}/dwi2response msmt_5tt -mask ${mask} -fslgrad ${bvecs} ${bvals}  ${dwi} ${tissues} ${wm} ${gm} ${csf} 

