"""

"""


import os
import pandas as pd
import numpy as np
from scipy import stats as stat





def sample_subjects(metadata, nb_subjects=50,alpha=0.01):
    """
    Sample at random men and female subjects such as the two groups are well balanced (same number of subjects in each
    group) and that the distribution of Age_in_Yrs in statistically non different between the two groups
    :param metadata: dataframe containing the potential subjects of interest and the whole metadata
    :return: selected subjects HCP ids
    """
    male = metadata.loc(metadata['Gender'] == 'M')
    female = metadata.loc(metadata['Gender'] == 'F')
    p = 0.0
    while p < alpha:
        s_female = female.sample(nb_subjects)
        s_male = male.sample(nb_subjects)

        dist_male = np.array(s_male['Age_in_Yrs'])
        dist_female = np.array(s_female['Age_in_Yrs'])
        #testing statistically that the two distributions are identical
        t, p = stat.wilcoxon(dist_male, dist_female)

    index_f = np.array(s_female['Subjects'])
    index_m = np.array(s_male['Subjects'])
    index = np.concatenate((index_m, index_f))
    selected_subjects = np.sort(index)

    return selected_subjects


def add_selection_index(metadata, subjects_selected):
    """
     Add an index to specify which subjects were selected (by any criterion)
    :param metadata:
    :param subjects_selected:
    :return:
    """
    selected = np.zeros(metadata.shape[0],dtype=bool)
    metadata['Selected'] = selected
    metadata['Selected'][metadata.Subject.isin(subjects_selected.tolist())] = True
    return metadata


def export_sampled_subjects(metadata):

    sampled_subjects = metadata.loc[metadata['Selected' == True],:]
    return sampled_subjects






if __name__ == '__main__':

    from variables import DIR_PHENO

    path_subjects = os.path.join(DIR_PHENO,'potential_subjects.csv')
    subjects = pd.read_csv(path_subjects)

    sampled_subjects_list = sample_subjects(subjects, 50, alpha=0.01)
    add_selection_index(subjects,sampled_subjects_list)
    #subjects.to_csv()
    sampled_subjects = export_sampled_subjects(subjects)
    sampled_subjects.to_csv(os.path.join(DIR_PHENO,'selected_subjects.csv'))











