"""
Given a pool of subjects create a txt file containing the list of the subjects to copy according to the HArdDrive
Useful to copy automatically all the subjects of interest at once using  the d.setup_dataset.sh script
"""

import os
import pandas as pd
from libs.subjects_selection.subjects_selection import subjects_by_disk


def main(path_metadata, path_base):
    """
    :param path_metadata: path to
    :param path_base:
    :return:
    """

    if not os.path.exists(path_base):
        os.makedirs(path_base)
    metadata = pd.read_csv(path_metadata)
    subjects_by_disk(metadata, path_base)




if __name__ =='__main__':



    from variables import DIR_PHENO
    path_meta ='/hpc/meca/users/pron.a/new_subjects.csv'
    path_disk = '/hpc/meca/users/pron.a/disks'
    meta = pd.read_csv(path_meta)
    subjects_by_disk(meta,path_disk)















