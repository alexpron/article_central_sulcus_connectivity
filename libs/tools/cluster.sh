#!/bin/bash

#-------------------------------------------------- INT Cluster Related Functions -------------------------------------#
# The functions beneath are wrapping of the frioul_batch command available on the head of the INT HPC cluster. They are
# designed to launch computations by subject either for commands or specific applications. The idea is to iterate on
# subjects of a database and have them treated in a parallel manner.
#----------------------------------------------------------------------------------------------------------------------#

source ../usual.sh

launch_subject_cmd()
{ cmd=$1
  subject=$2
  dir_cluster=$3
  core=${4-'12'}
  echo "command ${cmd}"
  echo "directory ${dir_cluster}"
  echo "subject ${subject}"
  echo "core ${core}"

  stderr=${dir_cluster}'/'${subject}'.stderr'
  stdout=${dir_cluster}'/'${subject}'.stdout'
  cmd_file=${dir_cluster}'/'${subject}'.cmd'
  rm_existing_file ${stderr}
  rm_existing_file ${stdout}
  rm_existing_file ${cmd_file}

  #command on passive
  frioul_batch  -c ${core} -d ${dir_cluster} -E ${stderr} -O ${stdout} -C ${cmd_file} "${cmd}"
}

#instanciate cluster useful file for one subject
launch_subject_bvproc()
{ bv_proc=$1
  subject=$2
  dir_cluster=$3
  brainvisa_instance=$4
  core=${5-'4'}

  stderr=${dir_cluster}'/'${subject}'.stderr'
  stdout=${dir_cluster}'/'${subject}'.stdout'
  cmd=${dir_cluster}'/'${subject}'.cmd'
  rm_existing_file ${stderr}
  rm_existing_file ${stdout}
  rm_existing_file ${cmd}
  ${DIR_SCRIPTS}/run_bv_proc.sh ${bv_proc} ${dir_cluster} ${stderr} ${stdout} ${cmd} ${brainvisa_instance} ${core}
 }










