import os
import numpy as np
from dipy.io import read_bvals_bvecs
from commit import trk2dictionary, core, models, operator
from amico import scheme
from configuration.configuration import BRAINVISA_DB, CENTER, DIR_SUBJECT_BRAINVISA


def dipy_to_commit(fbvals, fbvecs, path_out,complete_scheme=False, gradient=None, big_delta=0.0431, small_delta=0.0106, echo_time=0.089):
    """
    Regroup metadata (bvals and bvecs to a format recognize as input
    by COMMIT (here AMICO actually)
    :param fbvals: path of the bvals file
    :param fbvecs: path of the bvecs file
    :param path_out: path of metadata file
    :return:
    """
    bvals,bvecs = read_bvals_bvecs(fbvals, fbvecs)
    if not complete_scheme:
        out_metadata = np.zeros((len(bvals), 4))
        out_metadata[:,:-1] = bvecs[:]
        out_metadata[:,-1] = bvals[:]
    else:
        out_metadata = np.zeros((len(bvals), 7))
        out_metadata[:, :3] = bvecs[:]
        out_metadata[:, 4] = big_delta
        out_metadata[:, 5] = small_delta
        out_metadata[:, 6] = echo_time
        if gradient is not None:
            out_metadata[:, 3] = gradient
        else:
            out_metadata[:, 3] = np.sqrt(bvals[:]/(out_metadata[:, 4] - (out_metadata[:, 5]/3.0)))*(0.001/(267.513*out_metadata[:,5]))

    np.savetxt(path_out, out_metadata)
    return out_metadata

def commit_filtering(subject):
    dir_study = os.path.join(BRAINVISA_DB, CENTER)
    dir_subject = DIR_SUBJECT_BRAINVISA[subject]

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

    mit = core.Evaluation(dir_study, subject)
    relative_path_dmri = os.path.join('dmri', dwi_acq, dwi_proc, 'corrected_dwi_' + sub + '.nii.gz')
    relative_path_scheme = os.path.join('dmri', dwi_acq, dwi_proc, 'commit_metadata.txt')
    b0_thr = 50
    mit.load_data(relative_path_dmri, relative_path_scheme, b0_thr)
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
    pass