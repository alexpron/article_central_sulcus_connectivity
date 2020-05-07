"""

"""


import os
import pandas as pd
from libs.subjects_selection.subjects_selection import sample_subjects, add_selection_index, export_sampled_subjects




if __name__ == '__main__':

    from configuration.configuration import DIR_PHENO

    path_subjects = os.path.join(DIR_PHENO,'potential_subjects.csv')
    subjects = pd.read_csv(path_subjects)

    sampled_subjects_list = sample_subjects(subjects, 50, alpha=0.01)
    add_selection_index(subjects, sampled_subjects_list)
    sampled_subjects = export_sampled_subjects(subjects)
    sampled_subjects.to_csv(os.path.join(DIR_PHENO,'selected_subjects.csv'))











