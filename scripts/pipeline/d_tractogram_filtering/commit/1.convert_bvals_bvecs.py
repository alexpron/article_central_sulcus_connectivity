import os
import numpy as np
from re import match as re_match
from dipy.io import read_bvals_bvecs
from tools.tools import read_subjects_list
import amico.scheme






if __name__ =='__main__':

    HCP_db = os.environ["HCP_DATASET"]
    BV_db = os.environ["BV_DB"]
    dwi_acq = os.environ["DWI_ACQ"]
    dwi_proc = os.environ["DWI_PROC"]

    subjects_list = read_subjects_list(os.environ["SUBJ_LIST"])
    for sub in subjects_list:
        fbvals = os.path.join(HCP_db,sub,'T1w','Diffusion','bvals')
        fbvecs = os.path.join(HCP_db, sub, 'T1w', 'Diffusion', 'bvecs')
        commit_meta = os.path.join(BV_db,sub,'dmri',dwi_acq,dwi_proc,'commit_metadata.txt')
        dipy_to_commit(fbvals,fbvecs,commit_meta,complete_scheme=False)

