import numpy as np
from dipy.io import read_bvals_bvecs


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
        out_metadata[:,:3] = bvecs[:]
        out_metadata[:, 4] = big_delta
        out_metadata[:, 5] = small_delta
        out_metadata[:, 6] = echo_time
        if gradient is not None:
            out_metadata[:, 3] = gradient
        else:
            out_metadata[:, 3] = np.sqrt(bvals[:]/(out_metadata[:, 4] - (out_metadata[:, 5]/3.0)))*(0.001/(267.513*out_metadata[:,5]))

    np.savetxt(path_out, out_metadata)
    return out_metadata
