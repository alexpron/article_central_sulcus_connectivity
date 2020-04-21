#!/bin/bash

SubjectDIR=$1
SubjectID=$2
#setting default_values for HCP_DATASET
T1=${3}
T2=${4}
T1_brain=${5}
expert_file=${6}


recon-all -i ${T1} -T2 ${T2} -subjid ${SubjectID} -sd ${SubjectDIR} -motioncor -talairach -nuintensitycor -normalization -hires -3T
#removed the conform option not to be constrained to 1mm size --conform
mri_convert ${T1_brain} ${SubjectDIR}/${SubjectID}/mri/brainmask.mgz
mri_em_register -mask ${SubjectDIR}/${SubjectID}/mri/brainmask.mgz ${SubjectDIR}/${SubjectID}/mri/nu.mgz ${FREESURFER_HOME}/average/RB_all_2016-05-10.vc700.gca ${SubjectDIR}/${SubjectID}/mri/transforms/talairach_with_skull.lta
mri_watershed -T1 -brain_atlas ${FREESURFER_HOME}/average/RB_all_withskull_2016-05-10.vc700.gca "$SubjectDIR"/"$SubjectID"/mri/transforms/talairach_with_skull.lta "$SubjectDIR"/"$SubjectID"/mri/T1.mgz "$SubjectDIR"/"$SubjectID"/mri/brainmask.auto.mgz
cp "$SubjectDIR"/"$SubjectID"/mri/brainmask.auto.mgz "$SubjectDIR"/"$SubjectID"/mri/brainmask.mgz

recon-all -subjid ${SubjectID} -sd ${SubjectDIR} -autorecon2 -autorecon3 -3T -hires -T2pial -expert ${expert_file}

