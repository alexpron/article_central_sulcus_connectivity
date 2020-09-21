import os
import numpy as np
import pandas as pd
from scipy.linalg import norm
from variables import DIR_IN, DIR_OUT


def build_rot_matrix_2D(theta):
    affine = np.zeros((3, 3))
    affine[0, 0] = np.cos(theta)
    affine[1, 0] = np.cos(theta)
    affine[2, 2] = 1
    affine[0, 1] = -np.sin(theta)
    affine[1, 0] = np.sin(theta)
    return affine


def project_vector(data, v):
    # normalize the projection vector to have an orthonormal basis
    n = norm(v)
    v = v / n
    coord = np.zeros(len(data))
    for i in range(len(data)):
        d = data[i]
        coord[i] = np.vdot(d, v)
    return coord


if __name__ == "__main__":

    path_df = os.path.join(DIR_OUT, "init_tables", "coordinates.csv")
    df = pd.read_csv(path_df, index_col=0)
    df["Diag_Coord_Aligned"] = np.Inf
    df["Orth_Coord_Aligned"] = np.Inf
    df["Diag_Coord_Iso"] = np.Inf
    df["Orth_Coord_Iso"] = np.Inf
    data_aligned = df[["Pre_Coord_Aligned", "Post_Coord_Aligned"]].values
    data_iso = df[["Pre_Coord_Iso", "Post_Coord_Iso"]].values
    # diagonal axis
    v1 = np.array([1, 1])
    v2 = np.array([-1, 1])
    basis = [v1, v2]
    # projection of the first coordinate
    data_new_aligned = np.zeros_like(data_aligned)
    data_new_iso = np.zeros_like(data_iso)

    for i, v in enumerate(basis):
        data_new_aligned[:, i] = project_vector(data_aligned, v)
        data_new_iso[:, i] = project_vector(data_iso, v)
    df["Diag_Coord_Aligned"] = data_new_aligned[:, 0]
    df["Orth_Coord_Aligned"] = data_new_aligned[:, 1]
    df["Diag_Coord_Iso"] = data_new_iso[:, 0]
    df["Orth_Coord_Iso"] = data_new_iso[:, 1]

    df.to_csv(os.path.join(DIR_OUT, "inter_tables", "coordinates.csv"), index=False)
