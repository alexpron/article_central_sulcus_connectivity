#!/bin/bash

dwi=$1
bvecs=$2
bvals=$3
b0=$4

source ../../../../configuration/set_env.sh
#for mrtrix on the cluster (different shell migth not call bashrc)
mrtrix_bin=${6-${MRTRIX}}
${mrtrix_bin}/dwiextract ${dwi} -bzero -fslgrad $bvecs $bvals | ${mrtrix_bin}/mrmath - mean ${b0} -axis 3 -force

