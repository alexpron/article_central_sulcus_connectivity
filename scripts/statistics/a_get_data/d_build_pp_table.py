import pandas as pd

if __name__ == '__main__':
    from configuration.configuration import PPFM_TABLES, PPFM_DF

    df = pd.read_csv(PPFM_TABLES['final'])
    df = df[['Subject', 'Hemisphere', 'PP_CS_Coord_Iso', 'PP_Pre_Coord_Iso', 'PP_Post_Coord_Iso', 'PP_CS_Depth']]
    df['Subject'] = df['Subject'].astype(int)
    df.to_csv(PPFM_DF, index=False)
