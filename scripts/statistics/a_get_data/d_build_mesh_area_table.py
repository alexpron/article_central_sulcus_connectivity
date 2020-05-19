import pandas as pd


def read_mesh_area_df(path_dataframe):
    """
    :param path_dataframe:
    :return:
    """
    df = pd.read_csv(path_dataframe, sep='\t')
    df = df.iloc[:-1, :]
    df.loc[df['side'] == "left", ['side']] = "L"
    df.loc[df['side'] == "right", ['side']] = "R"
    df = df.rename(index=str, columns={'side': 'Hemisphere', 'subject': 'Subject', 'area': 'Mesh_Area'})
    df['Subject'] = df['Subject'].astype(int)
    return df


if __name__ == '__main__':
    from configuration.configuration import SIDES, AREA_TABLES, MESH_AREA_DF

    area_dfs = [read_mesh_area_df(AREA_TABLES[side]) for side in SIDES.keys()]
    d = pd.concat(area_dfs)
    d.to_csv(MESH_AREA_DF)
