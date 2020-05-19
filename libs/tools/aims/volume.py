import numpy as np
from soma import aims


def get_aims_to_RAS_transfo(path_volume, path_transformation):
    """
    Retrieve the estimated transformation between AIMS mm and RAS mm space
    :param path_volume:
    :param path_transformation:
    :return:
    """
    vol = aims.read(path_volume)
    aims_to_RAS = aims.AffineTransformation3d(vol.header()['transformations'][0])
    RAS_to_aims = aims_to_RAS.inverse()
    aff = np.array(aims_to_RAS.toMatrix())
    affine = np.array(RAS_to_aims.toMatrix())
    np.save(path_transformation, affine)
    return affine
