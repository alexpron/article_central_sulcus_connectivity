import pandas as pd

if __name__ == '__main__':
    from configuration.configuration import SELECTED

    subjects = pd.read_csv(SELECTED, index_col=0)
    # recode variables
    subjects['HandednessQ'] = pd.qcut(subjects['Handedness'], 2)
    subjects['AgeQ'] = pd.qcut(subjects['Age_in_Yrs'], 3)
    subjects['PMAT24_A_CR_Q'] = pd.qcut(subjects['PMAT24_A_CR'], 3, ['Low', 'Medium', 'High'])

    print(subjects['HandednessQ'].describe())
    subjects.to_csv(os.path.join(DIR_OUT, 'inter_tables', 'subjects.csv'))
