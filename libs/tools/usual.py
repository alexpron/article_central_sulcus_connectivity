"""

"""

import os

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