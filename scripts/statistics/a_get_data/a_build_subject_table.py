import pandas as pd

if __name__ == '__main__':
    from configuration.configuration import SUBJ_LIST, FULL, SELECTED

    # variables of interest for the study
    variables = ['Subject', 'Gender', 'Age_in_Yrs', 'Handedness', 'PMAT24_A_CR', 'Dexterity_AgeAdj', 'Strength_AgeAdj']
    # retrieving the whole data HCP metadata dataframe and extracting the selected subjects and variables of interests
    df = pd.read_csv(FULL)
    selected = df.loc[df['Subject'].isin(SUBJ_LIST), variables]
    selected.to_csv(SELECTED)
