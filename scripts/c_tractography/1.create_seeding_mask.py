from soma import aims
import os
import numpy as np
#This script create a seeding mask for tractography (it is accurate to use a good
#seeding mask in order to increase computationnal efficiency

#retrieving bash metavariable (remark set_env file must have been sourced first)
BV_db = os.environ["BV_DB"]
path_subjects_list = os.environ["SUBJ_LIST"]
dwi_acq = os.environ["DWI_ACQ"]
dwi_proc = os.environ["DWI_PROC"]

subjects_list = np.loadtxt(path_subjects_list)
subjects_list = subjects_list.astype(int)

for i, sub in enumerate(subjects_list):
    print(sub)
    path_5ttvis = os.path.join(BV_db,str(sub),'dmri',dwi_acq,dwi_proc,'5ttvisu.nii.gz')
    tissues = aims.read(path_5ttvis)
    t = np.array(tissues,copy=False)
    t[(t<0.50)] = 0
    t[t!=0] = 1
    aims.write(tissues, os.path.join(BV_db,str(sub),'dmri',dwi_acq,dwi_proc,'seeding_mask.nii.gz' ))







