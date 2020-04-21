######################################################################################################################
#  Script regrouping useful functions to process HCP data (or other database) in bash
#  Python is now preferred other batch even if for copying securely file, managing directories and launching commands
# on HPC cluster, bash is more convenient. This module may be transposed to Python.
# authors: Alexandre Pron & Lucie Thiebault both PhD student under the supervision of Olivier COULON
# contact: alexandre.pron@gmail.com
######################################################################################################################

#-------------------------------------------General functions -------------------------------------------------------#
# Small functions (essentially wrappings of existing bash commands to handle files and directories
#--------------------------------------------------------------------------------------------------------------------#

#delete a file that already exists
rm_existing_file()
{
if [ -e $1 ]; then
     rm $1
fi
}

# get a list containing the subdirectories of a directory and store their path
get_subdir_list()
{
#rename input variables
dir=$1
list_files=$2
#test list_subdir existence
rm_existing_file ${list_files}
#go into the directory for following commands to work
cd ${dir}
list=$(ls -d */ | grep -v ${dir})
#read list of subdir and remove the / character
for subDir in ${list}
do
	subDirName=$(echo ${subDir} | awk -F'/' '{print $1}')
	echo ${subDirName} >> $list_files
done
#go back to initial directory
cd -
}

#create  a directory safely
create_dir()
{ if [ ! -d $1 ];then
     echo $1 'does not exist'
     mkdir -p $1
  fi
}