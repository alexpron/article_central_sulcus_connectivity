#!/hpc/meca/users/pron.a/softs/virtualenvs/diffusion/bin/python -u

import nibabel as nib
from commit import trk2dictionary, core, models, operator
from dipy.core.gradients import GradientTable
#from tools import read_subjects_list
from amico import scheme
import os
import pickle
import numpy as np
from nibabel.streamlines import Field
import sys
from glob import glob
from nibabel.orientations import aff2axcodes

HCP_db = os.environ["HCP_DATASET"]
BV_db = os.environ["BV_DB"]
dwi_acq = os.environ["DWI_ACQ"]
dwi_proc = os.environ["DWI_PROC"]




def commit_filtering(sub):
    dir_study = BV_db
    dir_subject = os.path.join(BV_db, sub)
    #trk = os.path.join('/envau/work/meca/users/pron.a/HCP_preprocessed',sub,'tracks.trk')
    trk = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'tractography', 'tracks.trk')
    commit_meta = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'commit_metadata.txt')
    dir_commit = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'commit')
    peaks = os.path.join(BV_db, sub, 'dmri', dwi_acq, dwi_proc, 'csd', 'MSMT', 'brain_fit', 'peaks.nii.gz')
    trk2dictionary.run(
        filename_trk=trk,
        path_out=dir_commit,
        filename_peaks=peaks,
        fiber_shift=0.5,
        peaks_use_affine=True,
        vf_THR=0.1,
        gen_trk=False
    )
    core.setup()

    mit = core.Evaluation(BV_db, sub)
    relative_path_dmri = os.path.join('dmri', dwi_acq, dwi_proc, 'corrected_dwi_' + sub + '.nii.gz')
    relative_path_scheme = os.path.join('dmri', dwi_acq, dwi_proc, 'commit_metadata.txt')
    b0_thr = 50
    mit.load_data(relative_path_dmri, relative_path_scheme, b0_thr)
    #
    mit.set_model('StickZeppelinBall')
    #
    d_par = 1.7E-3  # Parallel diffusivity [mm^2/s]
    ICVFs = [0.7]  # Intra-cellular volume fraction(s) [0..1]
    d_ISOs = [1.7E-3, 3.0E-3]  # Isotropic diffusivitie(s) [mm^2/s]
    #
    mit.model.set(d_par, ICVFs, d_ISOs)
    #do not regenerate kernel or it migth create some bugs (one subject access to the kernel while being regenerated
    #by another one.
    mit.generate_kernels(regenerate=True)
    mit.load_kernels()
    mit.load_dictionary(dir_commit)

    mit.set_threads()
    mit.build_operator()
    mit.fit(tol_fun=1e-3, max_iter=1000)
    mit.save_results()

    # path_coefficients = os.path.join(dir_commit,'Results_StickZeppelinBall','results.pickle')
    # path_filtered_trk = os.path.join(dir_commit,'Results_StickZeppelinBall','filtered_tracks.trk')
    # filtered_trk(trk,path_coefficients,path_filtered_trk)

    #cleaning directories
    files_to_remove = glob(os.path.join(dir_commit,'*.dict'))
    for f in files_to_remove:
        os.remove(f)




if __name__ == '__main__':

    HCP_db = os.environ["HCP_DATASET"]
    BV_db = os.environ["BV_DB"]
    dwi_acq = os.environ["DWI_ACQ"]
    dwi_proc = os.environ["DWI_PROC"]

    subj = sys.argv[1]
    commit_filtering(subj)


















