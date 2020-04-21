"""
Get the list of HCP subjects used in the study directly from the dataset directory.
Useful to check the copy and take into account external modifications.
"""

import os
import numpy as np
import sys

def get_subdirectories(directory):
    """
    List only the direct subdirectories of a given directory.
    Files are not included (difference with os.listdir)
    :param directory: path of the directory string
    :return: subdirectories
    :rtype: list
    """
    subdirectories = os.walk(directory).next()[1]
    return subdirectories

def update_subjects_list(dataset_directory, path_subjects_list):
    """
    Check the  subjects stored in the dataset and save their identifier (HCP index)
    in a txt file.
    """
    subjects_list = get_subdirectories(dataset_directory)
    subjects_list = np.array(subjects_list, dtype=int)
    np.savetxt(path_subjects_list, subjects_list)
    return subjects_list
    

if __name__ == '__main__':

    #import is done at this level to avoid crash if function is just imported
    from variables import DIR_DATASET
    #use txt file, more convenient to read and inspect subjects
    path_subjects_list = os.path.join(DIR_DATASET,'subjects_list.txt')
    subjects_list = update_subjects_list(DIR_DATASET, path_subjects_list)
   

