"""
Some HCP subjects were found to have Quality check issues after their inclusion and processing.
Few subjects were thus, excluded and replaced during the study using this script. However, now that the QC_Issue field is included, and that subjects
were selected this script is useless and is  just kept for the sake of clarity and transparency about what
was done in the study.
"""



if __name__ == '__main__':
    import pandas as pd
    from libs.subjects_selection.subjects_selection import select_identical_subjects

    subj_with_qc_issues = pd.read_csv('/envau/work/meca/data/HCP/phenotype/output/subjects_to_reprocess.csv')
    potentials_subjects_2_reprocess = pd.read_csv('/envau/work/meca/data/HCP/phenotype/output/subjects_potentials_for_reprocessing.csv')
    new_subjects = select_identical_subjects(d1,d2)

