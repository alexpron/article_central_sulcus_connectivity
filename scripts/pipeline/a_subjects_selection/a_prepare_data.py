"""
First step of the subject selection process used for this study :
   + gather HCP metadata csv files
   + select subjects without quality check issues
   + select all subjects respecting inclusion criteria decided
"""

if __name__ == '__main__':

    from libs.subjects_selection.subjects_selection import complete_data, exclude_subjects_with_QC_issues, \
        extract_valid_subjects
    from configuration.configuration import RESTRICTED, UNRESTRICTED, FULL, CLEAN, POTENTIALS

    full_data = complete_data(RESTRICTED, UNRESTRICTED)
    full_data.to_csv(FULL)

    #exclude subjects with qc_issues
    ok_subjects = exclude_subjects_with_QC_issues(full_data)
    ok_subjects.to_csv(CLEAN)
    #select subjects respecting study criteria
    potential_subjects = extract_valid_subjects(ok_subjects)
    potential_subjects.to_csv(POTENTIALS)


