#!/bin/bash

############################################################################
# Initialisation script of the whole processing of Human Connectome Project
# dataset. This allows to access variables declared here in all the shells
# on the cluster and avoid copy of variables
# This script need to be sourced prior to any computation, e,g consider adding
# a source path/to/this/script.sh in your bash_personal ou bashrc
#TODO: move the content of this file to .json file

#Directory where the preprocessed data selected from HCP disks are copied
HCP_DATASET='/envau/work/meca/data/HCP/data/HCP_dataset'
export HCP_DATASET
#list of the subjects in HCP_DATASET obtained automatically
SUBJ_LIST="${HCP_DATASET}/subjects_list.txt"
export SUBJ_LIST
#FreeSurfer Database containing HCP subjects processed with FreeSurfer 6 from
# the output data of PreFreeSurferPipeline
FS_DB='/hpc/meca/data/U_Fibers/FS_database'
export FS_DB
#Brainvisa Database containing HCP subjects
BV_DB='/hpc/meca/data/U_Fibers/BV_database/subjects'
export BV_DB
#Specifying Structural and DWI acquisition names
STRUCT_ACQ='HCP_pipeline_modified'
export STRUCT_ACQ
DWI_ACQ='default_acquisition'
export DWI_ACQ
STRUCT_PROC='default_analysis'
export STRUCT_PROC
DWI_PROC='HCP_pipeline'
export DWI_PROC
#model instances:
CSD_MODEL='MSMT'
export CSD_MODEL
DTI_MODEL='Mrtrix'
FIT_INSTANCE='brain_fit'
export DTI_MODEL
export FIT_INSTANCE

#
#directories for bvproc and cluster on frioul
DIR_HOME='/hpc/meca/users/pron.a/HCP'
export DIR_HOME
DIR_CLUSTER="${DIR_HOME}/cluster"
export DIR_CLUSTER
DIR_BVPROC="${DIR_HOME}/bvproc"
export DIR_BVPROC

DIR_SCRIPTS="${DIR_HOME}/scripts"
export DIR_SCRIPTS

DIR_BVPROC_TEMPLATES="${DIR_SCRIPTS}/bv_proc_templates"
export DIR_BVPROC_TEMPLATES

#source with relative path
source "../libs/tools/tools.sh"

create_dir ${DIR_CLUSTER}
create_dir ${DIR_BVPROC}

#Brainvisa
BRAINVISA='/hpc/meca/users/pron.a/softs/brainvisa-4.6.1'
export BRAINVISA
#Mrtrix binary
MRTRIX='/hpc/meca/softs/mrtrix/bin'
export MRTRIX

#This subject is the first one of the subject list and was used as model in all bvprocs files
SUBJECT_TEST='100206'
export SUBJECT_TEST

clear









