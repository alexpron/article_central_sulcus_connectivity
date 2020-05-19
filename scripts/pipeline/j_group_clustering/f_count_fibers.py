import os
import numpy as np
import pandas as pd
from variables import DIR_OUT, DIR_DATA,SUBJ_LIST, SIDES
import seaborn as sns
from matplotlib import pyplot as plt


if __name__ == '__main__':
    # density with aligned knob
    d = 'global_mean'
    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index.npy')
    dir_output = os.path.join(DIR_OUT, 'group_clustering', 'dbscan_fixed')
    # original clusters (3) obtained using dbscan.
    path_sorted_labels = os.path.join(dir_output, d + '_' + 'sorted_labels' + '.npy')

    labels = np.load(path_sorted_labels)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index,2)
    subjects = np.zeros(hemispheres_index.size)
    hemispheres = np.zeros(hemispheres_index.size,dtype=object)
    hemispheres[side_index == 0] = 'L'
    hemispheres[side_index == 1] = 'R'


    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            index = i*len(SIDES) + j
            subjects[hemispheres_index == index] = int(subject)

    df = pd.DataFrame({'Subject': subjects,'Hemisphere':hemispheres,'Cluster':labels})

    df_no_noise = df.loc[df['Cluster']!=-1]

    hemi = df.groupby('Hemisphere').size()
    hemi_no_noise = df_no_noise.groupby('Hemisphere').size()
    ratio_h = 100*hemi_no_noise/hemi
    print ratio_h

    sub_level = df.groupby(['Hemisphere','Subject']).size()
    sub_level_no_noise = df_no_noise.groupby(['Hemisphere','Subject']).size()

    ratio_s = 100*sub_level_no_noise/sub_level

    L_s = ratio_s[('L',)].values
    R_s = ratio_s[('R',)].values

    #ratio_s.loc()

    # fig, ax = plt.subplots()
    # plt.title("Percentage of fibers kept with Group-level clustering \n by Brain Hemisphere ")
    # plt.plot(L_s, linewidth=3, label="Left Hemisphere")
    # plt.plot(R_s,linewidth=3,label=" Right Hemisphere")
    # plt.xlabel('Subject Ids')
    # plt.ylabel('Percentage')
    # plt.xticks(np.arange(0,100,5),SUBJ_LIST[::5],rotation=30)
    # plt.grid(axis='x')
    # plt.legend()
    # plt.show()

    clust_level = df_no_noise.groupby(['Hemisphere','Subject','Cluster']).size()
    ratio_0 = 100 * clust_level[(slice(None), slice(None),0)]/sub_level
    ratio_1 = 100 * clust_level[(slice(None), slice(None), 1)] / sub_level
    ratio_2 = 100 * clust_level[(slice(None), slice(None), 2)] / sub_level
    ratio_3 = 100 * clust_level[(slice(None), slice(None), 3)] / sub_level
    ratio_4 = 100 * clust_level[(slice(None), slice(None), 4)] / sub_level

    L_ratio_0 = ratio_0[('L',)].values
    L_ratio_1 = ratio_1[('L', )].values
    L_ratio_2 = ratio_2[('L', )].values
    L_ratio_3 = ratio_3[('L', )].values
    L_ratio_4 = ratio_0[('L', )].values

    R_ratio_0 = ratio_0[('R', )].values
    R_ratio_1 = ratio_1[('R', )].values
    R_ratio_2 = ratio_2[('R', )].values
    R_ratio_3 = ratio_3[('R', )].values
    R_ratio_4 = ratio_4[('R', )].values





    fig, axes = plt.subplots(2,sharex=True,sharey=True)
    plt.title("Percentage of fibers kept with Group-level clustering \n by Brain Hemisphere and Cluster ")

    axes[0].plot(L_ratio_0, linewidth=2,color='darkred', label="Cluster 0")
    axes[0].plot(L_ratio_1, linewidth=2, color='darkblue', label="Cluster 1")
    axes[0].plot(L_ratio_2, linewidth=2, color='orange', label="Cluster 2")
    axes[0].plot(L_ratio_3, linewidth=2, color='darkgreen', label="Cluster 3")
    axes[0].plot(L_ratio_4, linewidth=2, color='purple', label="Cluster 4")
    axes[0].grid(axis='x')

    axes[1].plot(R_ratio_0, linewidth=2, color='darkred', label="Cluster 0")
    axes[1].plot(R_ratio_1, linewidth=2, color='darkblue', label="Cluster 1")
    axes[1].plot(R_ratio_2, linewidth=2, color='orange', label="Cluster 2")
    axes[1].plot(R_ratio_3, linewidth=2, color='darkgreen', label="Cluster 3")
    axes[1].plot(R_ratio_4, linewidth=2, color='purple', label="Cluster 4")
    axes[1].grid(axis='x')

    plt.xlabel('Subject Ids')
    plt.ylabel('Percentage')
    plt.xticks(np.arange(0,100,5),SUBJ_LIST[::5],rotation=30)
    plt.grid(axis='x')
    plt.legend()
    plt.show()
















    #
    #  = df_no_noise.groupby(['Hemisphere', 'Subject', 'Cluster']).transform('size')
    #
    # print toto
    # print toti




























