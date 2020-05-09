"""
A collection of basic python functions useful to simplify life.
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

def merge_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z