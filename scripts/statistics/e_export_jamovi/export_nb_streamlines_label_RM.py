import os
import pandas as pd
from variables import DIR_OUT, DIR_JAM

if __name__ == "__main__":

    df = pd.read_csv(
        os.path.join(DIR_OUT, "derived_tables", "nb_streamlines_label_level.csv")
    )
    df = df.loc[df["Label"] != -1]
    print
    df.head()

    subgroups = df.groupby("Hemisphere")
    L = subgroups.get_group("L")
    R = subgroups.get_group("R")

    variables = ["Nb_Streamlines_Label"]

    # shameless hack to avoid renamming when merging
    R = R[["Subject"] + variables]

    L_variables = [v + "_" + "L" for v in variables]
    R_variables = [v + "_" + "R" for v in variables]
    A_variables = [v + "_" + "Asymmetry" for v in variables]

    d_L = {v: L_variables[i] for i, v in enumerate(variables)}
    d_R = {v: R_variables[i] for i, v in enumerate(variables)}

    L = L.rename(index=str, columns=d_L)
    L = L.reset_index(drop=True)
    R = R.rename(index=str, columns=d_R)
    R = R.reset_index(drop=True)

    final = pd.concat([L, R], axis=1)
    # print final.shape
    final = final.drop(columns="Hemisphere")
    # print final.head()

    # second step
    subsubgroups = final.groupby("Label")
    first = subsubgroups.get_group(0)
    second = subsubgroups.get_group(1)
    third = subsubgroups.get_group(2)
    fourth = subsubgroups.get_group(3)
    fifth = subsubgroups.get_group(4)

    varso = ["Nb_Streamlines_Label_L", "Nb_Streamlines_Label_R"]

    second = second[["Subject"] + varso]
    third = third[["Subject"] + varso]
    fourth = fourth[["Subject"] + varso]
    fifth = fifth[["Subject"] + varso]

    new_vars_0 = {
        "Nb_Streamlines_Label_L": "Nb_Streamlines_Label_L_" + str(0),
        "Nb_Streamlines_Label_R": "Nb_Streamlines_Label_R_" + str(0),
    }
    new_vars_1 = {
        "Nb_Streamlines_Label_L": "Nb_Streamlines_Label_L_" + str(1),
        "Nb_Streamlines_Label_R": "Nb_Streamlines_Label_R_" + str(1),
    }
    new_vars_2 = {
        "Nb_Streamlines_Label_L": "Nb_Streamlines_Label_L_" + str(2),
        "Nb_Streamlines_Label_R": "Nb_Streamlines_Label_R_" + str(2),
    }
    new_vars_3 = {
        "Nb_Streamlines_Label_L": "Nb_Streamlines_Label_L_" + str(3),
        "Nb_Streamlines_Label_R": "Nb_Streamlines_Label_R_" + str(3),
    }
    new_vars_4 = {
        "Nb_Streamlines_Label_L": "Nb_Streamlines_Label_L_" + str(4),
        "Nb_Streamlines_Label_R": "Nb_Streamlines_Label_R_" + str(4),
    }

    mygroups = [first, second, third, fourth, fifth]
    myvars = [new_vars_0, new_vars_1, new_vars_2, new_vars_3, new_vars_4]

    mygroups = [g.rename(index=str, columns=myvars[i]) for i, g in enumerate(mygroups)]
    mygroups = [g.reset_index(drop=True) for i, g in enumerate(mygroups)]

    real_final = pd.concat(mygroups, axis=1)
    print
    real_final.head()

    new_A_variables = ["Asymmetry_Streamlines_Label_" + str(i) for i in range(5)]
    new_variables_L = ["Nb_Streamlines_Label_L_" + str(i) for i in range(5)]
    new_variables_R = ["Nb_Streamlines_Label_R_" + str(i) for i in range(5)]

    for i, a in enumerate(new_A_variables):
        R_v = real_final[new_variables_R[i]].values
        L_v = real_final[new_variables_L[i]].values
        A = 2.0 * (R_v - L_v) / (R_v + L_v)
        real_final[a] = A
    print
    real_final.head()
    real_final.to_csv(
        os.path.join(DIR_JAM, "inter", "nb_streamlines_label_level_RM.csv"), index=False
    )
    # #
    # for label, subdf in final.groupby('Label'):
    #         subdf.reset_index(drop=True )
    #         print subdf.shape
    #         subdf.to_csv(os.path.join(DIR_JAM, 'inter', 'nb_streamlines_label_level_' + str(label) + '_RM.csv'), index=False)
    #
    #
