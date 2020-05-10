#!/bin/bash

source "../../../../configuration/set_env.sh"
source "../../../tools/tools.sh"

conversion_script="/tck2trk.py"
sequence='tck2trk'

for subj in $(cat ${SUBJ_LIST})
do
    #echo "Processing subject ${subj}"
    tckfile="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/tractography/tracks.tck"
    trkfile="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/tractography/tracks.trk"
    if [ -e "${tckfile}" ] ; then
    #if  [ -e "${tckfile}" ] && [ ! -s "${trkfile}" ] ; then
        ref_volume="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/csd/MSMT/brain_fit/wm_fod.nii.gz"
        cmd=export PYTHONPATH='' ; ${BRAINVISA_PYTHON} ${conversion_script} ${ref_volume} ${tckfile} -f
        ${cmd}
        echo "$subj launched"
    fi
done





