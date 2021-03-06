import pandas as pd
from configuration.configuration import SIDES


def import_bv_fiedler_table(path_dataframe):
    """
    Read a fiedler lenght table generated by the associated BrainVISA process
    and reformat it
    :param path_dataframe:
    :return:
    """
    df = pd.read_csv(path_dataframe, sep="\t")
    df = df.d1.iloc[:-1, :]
    # reencode dataframe tab
    for side in SIDES.keys():
        df.loc[df["side"] == SIDES[side], ["side"]] = side
        df = df.rename(
            index=str,
            columns={
                "side": "Hemisphere",
                "subject": "Subject",
                "fidler_length": "Fiedler_Length",
            },
        )
    return df


if __name__ == "__main__":
    from configuration.configuration import SIDES, FIEDLER_TABLES, FIEDLER_DF

    fiedler_dfs = [
        import_bv_fiedler_table(FIEDLER_TABLES[side]) for side in SIDES.keys()
    ]
    d = pd.concat(fiedler_dfs)
    # reencoding values to adopt common notation (for future merges)
    d["Subject"] = d["Subject"].astype(int)
    d.to_csv(FIEDLER_DF)
