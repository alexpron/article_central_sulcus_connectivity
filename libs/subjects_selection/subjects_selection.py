"""
HCP metadata (.csv) management functions (import, sort, merge databases) and criteria used
to select subjects from the Human Connectome Project (HCP).
"""

import os
import numpy as np
import pandas as pd
import scipy.stats as stat
from libs.tools.usual import get_subdirectories
from copy import copy


def create_disk_index():
    """
    S900 release of the  subjects are stored onto 8 physical hard drives.
    Till the whole S900 release has not been copied onto a dedicated storage place, subjects of interest must be selected
    and copied on the INT HCP Cluster
    :return: Information about first and last subject on a given HCP hard drive
    :rtype: List of dictionnaries
    """
    d1 = {'disk': 1, 'min_index': 100206, 'max_index': 128026}
    d2 = {'disk': 2, 'min_index': 128127, 'max_index': 154229}
    d3 = {'disk': 3, 'min_index': 154431, 'max_index': 178950}
    d4 = {'disk': 4, 'min_index': 179245, 'max_index': 209329}
    d5 = {'disk': 5, 'min_index': 209834, 'max_index': 371843}
    d6 = {'disk': 6, 'min_index': 377451, 'max_index': 587664}
    d7 = {'disk': 7, 'min_index': 588565, 'max_index': 783462}
    d8 = {'disk': 8, 'min_index': 784565, 'max_index': 996782}
    disks = [d1, d2, d3, d4, d5, d6, d7, d8]
    return disks


def add_drive_index(metadata):
    """
    HCP subjects are split onto several physical hard drive. This function add an index to be able to locate a given
    subject easily.
    :param metadata: dataframe with metadata about HCP subjects
    :return: metadata
    """
    disks = create_disk_index()
    #instanciating empty column
    e = np.zeros(metadata.shape[0], dtype=np.int)
    # Creating the correspondance
    for d in disks:
        e[(metadata['Subject'] >= d['min_index']) & (metadata['Subject'] <= d['max_index'])] = d['disk']
    #add the Hard_Drive column to the metadata dataset
    metadata['Hard_Drive'] = e
    return metadata

def merge_metadata(path_data1, path_data2, merge_var='Subject'):
    """
    Merge two HCP metadata dataframes into one dataframe. Merge is don by default on subject ID key

    :param path_data1: path of the unrestricted metadata  csv file
    :param path_data2: path of the unrestricted metadata  csv file
    :return: the dataframe containing all HCP metadata
    """

    data1 = pd.read_csv(path_data1)
    data2 = pd.read_csv(path_data2)
    full_data = pd.merge(data1, data2, on=merge_var)
    return full_data


def exclude_subjects_with_QC_issues(metadata, exclude_tags=('A','B','C','D','E')):

    """
    QC was performed on structural data essentially here is a sump up of the codes
    A : anatomical issues revealed on structural scans (T1 and T2)
    B : defaults on segmentation and surface obtained with FreeSurfer
    C : diffusion and fmRI data acquired during a period onf gradient instability (HCP recommands to exclude them)
    D : fmRI data presented a incohrence and was corrected a posteriori
    E : fmRI manually relabelled
    see   for more informations
    Since we study both structural and diffusion data we consider a subject as incorrect if his QC_Issue field
    any of the exclude tags. If you want to study fmRI consider excluding D and E subjects also.
    If you do not reprocess HCP data exclude B tag data also. Anyway if you start a new_study we recommand to exclude all
    the potential subjects eg [A,B,C, D,E] categories

    :param metadata: a metadata dataframe containing the QC_Issue field
    :return:
    """

    subjects = np.array(metadata['Subject'])
    qc_issue = np.array(metadata['QC_Issue'])
    #print qc_issue.dtype
    #by default all subjects are included
    valid_subjects = np.zeros(len(subjects),dtype=bool)
    for i, qc_tag in enumerate(qc_issue):
        if type(qc_tag) is not str: # there is at least one know issue
            #for t in exclude_tags:
                #if t in qc_tag:
            valid_subjects[i] = True
    metadata['OK_Subjects'] = valid_subjects
    valid_subjects = metadata.loc[metadata['OK_Subjects'] == True,:]
    return valid_subjects



def extract_valid_subjects(metadata):
    """
    Extract a subset of subjects that might be useful for our study. The selection criterion are the following

    - Having a diffusion MRI scan and a T1 MRI scan
    - Being right-handed (Handedness score > 50)
    - Twins are excluded

    :param metadata: the dataframe containing the whole subjects and the whole variables
    :return: potential subjects dataframe with all the variables
    """

    #selection is done in several steps for readability
    #subjects must have completed all the structural and diffusion session
    acquisition_cond = metadata.loc[((metadata['3T_Full_MR_Compl'] == True ) & (metadata['3T_dMRI_Compl'] == True)), :]
    #no twins (SR stands for Self Reported)
    twin_cond = acquisition_cond.loc[(acquisition_cond['ZygositySR'] == "NotTwin")]
    #strong right-handedness condition so that subject are more homogeneous
    handed_cond = twin_cond.loc[(twin_cond['Handedness'] >= 50), :]
    age_cond = handed_cond.loc[((handed_cond['Age_in_Yrs'] >= 20) & (handed_cond['Age_in_Yrs'] <= 40)), :]
    return age_cond


def complete_data(path_restricted, path_unrestricted):
    """
    Merge both restricted and unrestricted metadata and

    :param path_restricted: restricted metadata csv file path
    :param path_unrestricted: unrestricted metadata csv file path
    :return: full_data : dataframe containing the whole metadata and the location on HCP Hard Drives
    """
    metadata = merge_metadata(path_restricted, path_unrestricted)
    full_metadata = add_drive_index(metadata)
    return full_metadata


def build_proper_subjects_table(path_unrestricted, path_restricted, path_ok_subjects):
    """
    :param path_unrestricted:
    :param path_restricted:
    :param path_ok_subjects:
    :return:
    """
    #build dataframe containing all the metadata
    full_data = complete_data(path_unrestricted, path_restricted)
    #some subjects might not be appropriate for a study, exclude them
    ok_subjects = exclude_subjects_with_QC_issues(full_data)
    ok_subjects.to_csv(path_ok_subjects)
    pass


def subjects_by_disk(metadata, path_base):
    """
    Export a list of the selected subjects for each HCP Hard Drive
    :param metadata: dataframe contaiing the selected subjects and their associated hard drive
    :return:
    """
    meta = metadata[['Subject', 'Hard_Drive']]
    subjects_by_disk = meta.groupby('Hard_Drive')
    for s in subjects_by_disk:
        subjects = np.array([s[1]]['Subject'])
        np.savetxt(os.path.join(path_base, 'disk_' + str(s[0]) + '.txt'), subjects, fmt='%i')
    pass



def update_subjects_list(dataset_directory, path_subjects_list):
    """
    Check the  subjects stored in the dataset and save their identifier (HCP index)
    in a txt file.
    """
    subjects_list = get_subdirectories(dataset_directory)
    subjects_list = np.array(subjects_list, dtype=int)
    np.savetxt(path_subjects_list, subjects_list)
    return subjects_list


def sample_subjects(metadata, nb_subjects=50,alpha=0.01):
    """
    Sample at random men and female subjects such as the two groups are well balanced (same number of subjects in each
    group) and that the distribution of Age_in_Yrs in statistically non different between the two groups
    :param metadata: dataframe containing the potential subjects of interest and the whole metadata
    :return: selected subjects HCP ids
    """
    male = metadata.loc(metadata['Gender'] == 'M')
    female = metadata.loc(metadata['Gender'] == 'F')
    p = 0.0
    while p < alpha:
        s_female = female.sample(nb_subjects)
        s_male = male.sample(nb_subjects)

        dist_male = np.array(s_male['Age_in_Yrs'])
        dist_female = np.array(s_female['Age_in_Yrs'])
        #testing statistically that the two distributions are identical
        t, p = stat.wilcoxon(dist_male, dist_female)

    index_f = np.array(s_female['Subjects'])
    index_m = np.array(s_male['Subjects'])
    index = np.concatenate((index_m, index_f))
    selected_subjects = np.sort(index)

    return selected_subjects

def add_selection_index(metadata, subjects_selected):
    """
     Add an index to specify which subjects were selected (by any criterion)
    :param metadata:
    :param subjects_selected:
    :return:
    """
    selected = np.zeros(metadata.shape[0], dtype=bool)
    metadata['Selected'] = selected
    metadata['Selected'][metadata.Subject.isin(subjects_selected.tolist())] = True
    return metadata


def export_sampled_subjects(metadata):

    sampled_subjects = metadata.loc[metadata['Selected' == True],:]
    return sampled_subjects



def select_identical_subjects(d1,d2):
    """
    Some subjects coming from the initial selection were found to have QC_Issue a posteriori when the QC_Issue field
    was added by the HCP into the metadata file. This function try to select subjects as close as possible with respect
    with the first selection criteria.
    :param d1:
    :param d2:
    :return:
    """
    s1 = np.array(d1['Subject'])
    a1 = np.array(d1['Age_in_Yrs'])
    g1 = np.array(d1['Gender'])
    h1 = np.array(d1['Handedness'])

    s2 = np.array(d2['Subject'])
    a2 = np.array(d2['Age_in_Yrs'])
    g2 = np.array(d2['Gender'])
    h2 = np.array(d2['Handedness'])

    new_subjects = [s2[(a2 == a1[i])*(g2==g1[i])*h2==h1[i]] for i in range(len(s1))]
    new_subjects_approx = [s2[(a2 == a1[i]) * (g2 == g1[i])] for i in range(len(s1))]
    #First step exact remplacement
    new_subjects_final = np.zeros(len(new_subjects)).tolist()
    for i, subjects in enumerate(new_subjects):
        if len(subjects) == 0:
            new_subjects_final[i] = []
        else:
            for j in range(len(subjects)):
                 if subjects[j] not in new_subjects_final:
                     new_subjects_final[i] = subjects[j]
                     break
            # if new_subjects_final[i] == 0:
            #      new_subjects_final[i] = []

    #Second step approximate remplacement
    new_subjects_final2 = copy(new_subjects_final)
    for i, subject in enumerate(new_subjects_final2):
        #la liste est vide
        if not subject:
           hand_score = np.array([h2[s2 == s] for  s in new_subjects_approx[i]]).ravel()
           diff = np.abs(hand_score - h1[i])
           min_subject = np.array(new_subjects_approx[i],dtype=int)[np.argsort(diff)].tolist()
           for j in range(len(min_subject)):
               if min_subject[j] not in new_subjects_final2:
                   new_subjects_final2[i] = min_subject[j]
                   break
    return new_subjects_final2


