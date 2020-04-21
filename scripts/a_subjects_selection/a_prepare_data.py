"""

"""



if __name__ == '__main__':


    import os
    from libs.subjects_selection.subjects_selection import complete_data, exclude_subjects_with_QC_issues, \
        extract_valid_subjects
    from configuration.configuration import DIR_META


    path_restricted = os.path.join(DIR_META,'input','RESTRICTED_07_30_2018_S900_release.csv')
    path_unrestricted = os.path.join(DIR_META,'input','unrestricted_07_30_2018_S900_release.csv')

    path_full = os.path.join(DIR_META,'output', 'full_data.csv')
    path_ok = os.path.join(DIR_META,'output','full_data_without_qc_issues.csv')
    path_potential = os.path.join(DIR_META,'output','potential_subjects_for_study.csv')

    full_data = complete_data(path_restricted, path_unrestricted)
    full_data.to_csv(path_full)

    #exclude subjects with qc_issues
    ok_subjects = exclude_subjects_with_QC_issues(full_data)
    ok_subjects.to_csv(path_ok)
    #select subjects respecting study criteria
    potential_subjects = extract_valid_subjects(ok_subjects)
    potential_subjects.to_csv(path_potential)


