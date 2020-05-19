"""
A collection of basic python functions useful to simplify life.
"""

import os
import numpy as np

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


def merge_dicts(x, y):
    """
    Merge two dictionaries in Python
    :param x: a dictionary
    :param y: a dictionary
    :return: a dictionary
    """
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def get_subjects_list(dir_db, path_out=None):
    """
    :param dir_db:
    :param path_out:
    :return:
    """
    subjects = os.walk(dir_db).next()[1]
    subjects.sort()
    if path_out is not None:
      subjects_list = np.array(subjects,dtype=int)
      np.savetxt(path_out, subjects_list,fmt="%i")
    return subjects


def read_subjects_list(path_list):
    """
    :param path_list: path of the text file containing the IDs of the subjects
    :return: list of the subjects IDs as strings (easier for path completion)
    """
    subs = np.loadtxt(path_list)
    subjects_list = [str(int(s)) for s in subs]
    return subjects_list

