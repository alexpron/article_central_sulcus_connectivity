"""
Given a pool of subjects create a txt file containing the list of the subjects to copy according to the HArdDrive
Useful to copy automatically all the subjects of interest at once using the functions in 3.setup_dataset script
"""


import pandas as pd
import numpy as np
import os



def subjects_by_disk(metadata, path_base):
     """
     Export a list of the selected subjects for each HCP Hard Drive
     :param metadata: dataframe contaiing the selected subjects and their associated hard drive
     :return:
     """
     meta = metadata[['Subject','Hard_Drive']]
     subjects_by_disk = meta.groupby('Hard_Drive')
     for s in subjects_by_disk:
        subjects = np.array([s[1]]['Subject'])
        np.savetxt(os.path.join(path_base,'disk_' + str(s[0]) + '.txt'), subjects, fmt='%i')
     pass


def main(path_metadata, path_base):

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















