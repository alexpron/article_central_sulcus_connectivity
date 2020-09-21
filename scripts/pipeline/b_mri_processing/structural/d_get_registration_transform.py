from __future__ import print_function
import os
from soma import aims


def get_transformation(path_volume, path_reference_volume, path_transfo, path_inverse):
    volume = aims.read(path_volume)
    reference_volume = aims.read(path_reference_volume)
    header = volume.header()
    header_ref = reference_volume.header()
    transfo_vol_to_mni = aims.AffineTransformation3d(header["transformations"][0])
    transfo_reference_to_mni = aims.AffineTransformation3d(
        header_ref["transformations"][0]
    )
    final_transfo = transfo_reference_to_mni.inverse() * transfo_vol_to_mni
    inverse = final_transfo.inverse()
    aims.write(final_transfo, path_transfo)
    aims.write(inverse, path_inverse)
    pass


if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        T1_BRAINVISA,
        T1_2_DWI,
        DWI_2_T1,
        DWI_HCP,
    )

    for subject in SUBJ_LIST:
        if not os.path.exists(T1_BRAINVISA[subject]):
            print(
                "HCP subject ",
                subject,
                "has not been imported yet in HCP Brainvisa database",
            )
            pass
        else:
            get_transformation(
                T1_BRAINVISA[subject],
                DWI_HCP[subject],
                T1_2_DWI[subject],
                DWI_2_T1[subject],
            )
