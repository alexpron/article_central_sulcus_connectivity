"""
Select randomly 100 (5O Male, 50 Female) subjects from the potential subjects dataset
WARNING : this script should only be launched once !
"""

import pandas as pd
from libs.subjects_selection import (
    sample_subjects,
    add_selection_index,
    export_sampled_subjects,
)


def main(path_potential_subjects, path_selected_subjects):
    """
    :param path_potentials_subjects:
    :param path_selected_subjects:
    :return:
    """
    subjects = pd.read_csv(path_potential_subjects)
    sampled_subjects_list = sample_subjects(subjects, 50, alpha=0.01)
    add_selection_index(subjects, sampled_subjects_list)
    sampled_subjects = export_sampled_subjects(subjects)
    sampled_subjects.to_csv(path_selected_subjects)
    pass


if __name__ == "__main__":
    from configuration.configuration import POTENTIALS, SELECTED

    main(POTENTIALS, SELECTED)
