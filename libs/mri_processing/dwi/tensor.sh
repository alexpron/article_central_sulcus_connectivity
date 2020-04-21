#!/bin/bash

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
default_mrtrix_bin='/hpc/meca/softs/mrtrix/bin'
mrtrix_bin=${9-${default_mrtrix_bin}}
#launching the two command (remark piping is not working so use that
${mrtrix_bin}/dwi2tensor ${dwi} ${tensor} -mask ${mask}  -fslgrad ${bvecs} ${bvals}
${mrtrix_bin}/tensor2metric ${tensor} -fa ${FA} -adc ${MD}  -mask ${mask} -vector ${v1}

