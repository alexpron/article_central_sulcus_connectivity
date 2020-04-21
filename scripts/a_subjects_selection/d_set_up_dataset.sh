#!/bin/bash
########################################################################################################################
#              SECURED COPY SCRIPTS:
# Author: Alexandre Pron, PhD student (2015, 2019) under the supervision of Olivier COULON and Christine DERUELLE.
#
# Sum up:
# Data of the HCP subjects are till now split and stored on 8 storage hard drives. These scripts allows you to copy the
# data you are interested in (here preprocessed diffusion and structural data only. This is achieved using rsync. If
# the copy is interrupted (it may very often happen) you just need to launch again the copy and only remaining data will
# be copied.
#
########################################################################################################################



copy_subject_from_disk()
{
    #if the latest version of rsync (at least 3.1) is available. Allows a global estimation time and percetange
    #reeconding variables for the sake of clarity
    hard_drive=${1}
    subject_id=${2}
    dir_output=${3}

    input_subject="${hard_drive}/${subject_id}"
    rsync -avzh  --include="*/T1w" --exclude="unprocessed" --exclude="MNINonLinear" --exclude="Results"  --exclude="release-notes" --info=progress2 ${input_subject} ${dir_output}/

}
#
copy_disk_subjects()
{
    #rencoding variables for the sake of clarity
    hard_drive=${1}
    subjects_list=${2}
    dir_out=${3}

    for subject in $(cat ${subjects_list})
    do
       copy_subject_from_disk ${hard_drive} ${subject} ${dir_out}
    done
}


main(){

if [ -e $2 ] ; then
   copy_disk_subjects $1 $2 $3
else
   copy_subject_from_disk $1 $2 $3
fi
}

#copy_disk_subjects
