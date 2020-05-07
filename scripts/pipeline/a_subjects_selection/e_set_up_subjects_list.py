


if __name__ == '__main__':

    import os
    from configuration.configuration import DIR_DATASET
    from libs.subjects_selection.subjects_selection import update_subjects_list

    #use .txt file, more convenient than .csv to exploit using bash scripts
    path_subjects_list = os.path.join(DIR_DATASET,'subjects_list.txt')
    subjects_list = update_subjects_list(DIR_DATASET, path_subjects_list)
   

