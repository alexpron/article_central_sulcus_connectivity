"""
Some subjects presented Quality Check Isssues and needed to be replaced by new subjects with similar
characteristic (Gender, Age, Handedness)
"""

import numpy as np
import pandas as pd
from copy import copy

def select_identical_subjects(d1,d2):
    s1 = np.array(d1['Subject'])
    print "OK", s1.shape
    a1 = np.array(d1['Age_in_Yrs'])
    g1 = np.array(d1['Gender'])
    h1 = np.array(d1['Handedness'])

    s2 = np.array(d2['Subject'])
    a2 = np.array(d2['Age_in_Yrs'])
    g2 = np.array(d2['Gender'])
    h2 = np.array(d2['Handedness'])

    new_subjects = [s2[(a2 == a1[i])*(g2==g1[i])*h2==h1[i]] for i in range(len(s1))]
    print new_subjects
    new_subjects_approx = [s2[(a2 == a1[i]) * (g2 == g1[i])] for i in range(len(s1))]
    #First step exact remplacement
    new_subjects_final = np.zeros(len(new_subjects)).tolist()
    for i, subjects in enumerate(new_subjects):
        print i, subjects, len(subjects)
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
    print "Exact Subjects matching", new_subjects_final2
    for i, subject in enumerate(new_subjects_final2):
        #la liste est vide
        if not subject:
           print "Candidates potential", new_subjects_approx[i]
           hand_score = np.array([h2[s2 == s] for  s in new_subjects_approx[i]]).ravel()
           print "Hand", hand_score
           diff = np.abs(hand_score - h1[i])
           print "Orig", diff , '\n'
           print "Tri", np.sort(diff), '\n'
           min_subject = np.array(new_subjects_approx[i],dtype=int)[np.argsort(diff)].tolist()
           for j in range(len(min_subject)):
               if min_subject[j] not in new_subjects_final2:
                   new_subjects_final2[i] = min_subject[j]
                   break
    return new_subjects_final2








if __name__ == '__main__':

    d1 = pd.read_csv('/envau/work/meca/data/HCP/phenotype/output/subjects_to_reprocess.csv')
    d2 = pd.read_csv('/envau/work/meca/data/HCP/phenotype/output/subjects_potentials_for_reprocessing.csv')

    print d1.shape

    new_subjects = select_identical_subjects(d1,d2)

    print len(new_subjects)
    print new_subjects