#!/bin/bash

source ../../../../configuration/set_env.sh

#renaming arguments
dwi=$1
bvals=$2
bvecs=$3
mask=$4
tensor=$5
FA=$6
MD=$7
v1=$8


#for mrtrix on the cluster (different shell migth not call bashrc)

mrtrix_bin=${9-${MRTRIX}}
#launching the two command (remark piping is not working so use that
${mrtrix_bin}/dwi2tensor ${dwi} ${tensor} -mask ${mask}  -fslgrad ${bvecs} ${bvals}
${mrtrix_bin}/tensor2metric ${tensor} -fa ${FA} -adc ${MD}  -mask ${mask} -vector ${v1}

