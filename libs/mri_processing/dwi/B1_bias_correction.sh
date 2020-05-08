#!/bin/bash

#conversion of initial data to mrtrix format and
#B1 bias correction using Ants N4 correction

source ../../../../configuration/set_env.sh

dwi=$1
bvals=$2
bvecs=$3
dwi_corr=$4
mrtrix_bin=${5-${MRTRIX}}


${mrtrix_bin}/dwibiascorrect ${dwi} -fslgrad ${bvecs} ${bvals}  -ants  ${dwi_corr} -force





  
  
  
