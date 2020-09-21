"""

"""

import numpy as np


def get_hemisphere_group_pp(dataframe, subject, side):
    """

    :param dataframe:
    :param subject:
    :param side:
    :return:
    """
    pre_c = dataframe.loc[
        (dataframe["Subject"] == int(subject)) & (dataframe["Hemisphere"] == side),
        "PP_Pre_Coord_Global_Mean",
    ].iloc[0]
    post_c = dataframe.loc[
        (dataframe["Subject"] == int(subject)) & (dataframe["Hemisphere"] == side),
        "PP_Post_Coord_Global_Mean",
    ].iloc[0]
    pp = np.array([pre_c, post_c])
    return pp


def get_hemisphere_subject_pp(dataframe, subject, side):
    """
    :param dataframe:
    :param subject:
    :param side:
    :param PP_coord:
    :return:
    """
    pre_coord = dataframe.loc[
        (dataframe["Subject"] == int(subject)) & (dataframe["Hemisphere"] == side),
        "PP_Pre_Coord_Iso",
    ].iloc[0]
    post_coord = dataframe.loc[
        (dataframe["Subject"] == int(subject)) & (dataframe["Hemisphere"] == side),
        "PP_Post_Coord_Iso",
    ].iloc[0]
    pp = np.array([pre_coord, post_coord])
    return pp


def ppfm_coords_2_str(ppfm):
    """
    :param ppfm:
    :return:
    """
    return (
        "("
        + str(np.round(ppfm[0], decimals=2))
        + " ; "
        + str(np.round(ppfm[1], decimals=2))
        + ")"
    )
