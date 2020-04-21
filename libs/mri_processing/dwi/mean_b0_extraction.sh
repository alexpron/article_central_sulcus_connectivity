#!/bin/bash

dwi=$1
bvecs=$2
bvals=$3
b0=$4

#for mrtrix on the cluster (different shell migth not call bashrc)
default_mrtrix_bin='/hpc/meca/softs/mrtrix/bin'
mrtrix_bin=${6-${default_mrtrix_bin}}
${mrtrix_bin}/dwiextract ${dwi} - -bzero -fslgrad $bvecs $bvals | ${mrtrix_bin}/mrmath - mean ${b0} -axis 3 -force  

