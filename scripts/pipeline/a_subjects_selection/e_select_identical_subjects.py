"""
Some HCP subjects were found to have Quality check issues after their inclusion and processing.
Few subjects were thus, excluded and replaced during the study using this script. However, now that the QC_Issue field is included, and that subjects
were selected this script is useless and is  just kept for the sake of clarity and transparency about what
was done in the study.
"""


if __name__ == '__main__':

    import pandas as pd
    from libs.subjects_selection import select_identical_subjects
    from configuration.configuration import BAD_SUBJECTS, POTENTIALS

    subj_with_qc_issues = pd.read_csv(BAD_SUBJECTS)
    potentials_subjects = pd.read_csv(POTENTIALS)
    new_subjects = select_identical_subjects(subj_with_qc_issues, potentials_subjects)

