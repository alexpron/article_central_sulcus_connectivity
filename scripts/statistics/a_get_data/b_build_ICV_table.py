import os
import numpy as np
import pandas as pd


def get_ICV(aseg_stats_file):
    """
    Retrieve the Intra-Cranial Volume (ICV) value from the FreeSurfer aseg.stats file
    :param aseg_stats_file: path of the aseg.stats file
    :return: ICV value (float)
    """
    with open(aseg_stats_file, "r") as f:
        # the ICV line was checked to be 34
        line = f.readlines()[34]
    splitted_line = line.split(",")
    # the ICV measure was found to be on the third column
    ICV = float(splitted_line[3])
    return ICV


if __name__ == "__main__":

    from configuration.configuration import SUBJ_LIST, ASEGS, ICV_DF

    ICVs = np.zeros(len(SUBJ_LIST))
    for i, subject in enumerate(SUBJ_LIST):
        ICVs[i] = get_ICV(ASEGS[subject])
    df = pd.DataFrame({"Subject": np.array(SUBJ_LIST, dtype=int), "ICV": ICVs})
    df.to_csv(ICV_DF)
