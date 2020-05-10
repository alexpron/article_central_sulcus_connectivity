#!/bin/bash

source "${DIR_LIBS}/tools/tools.sh"
sequence='commit'
dir_cluster="${DIR_CLUSTER}/${sequence}"
create_dir ${dir_cluster}
echo ${dir_cluster}


for subj in $(cat ${SUBJ_LIST})
do  
    result="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/commit_final/Results_StickZeppelinBall/results.pickle"
    trk="${BV_DB}/${subj}/dmri/${DWI_ACQ}/${DWI_PROC}/tractography/tracks.trk"
    if [ ! -e "${result}" ] && [ -e "${trk}" ] && [ -s "${trk}" ] ; then
    	cmd="export PYTHONPATH=' ' ; ${DIR_SCRIPTS}/Tractography/commit/commit_filtering.py  ${subj}"
        #echo "The command is ${cmd}"
    	launch_subject_cmd "${cmd}" ${subj} ${dir_cluster} 12
    fi
done
