from libs.tools.aims.volume import get_aims_to_RAS_transfo


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST
    for subject in SUBJ_LIST:
        get_aims_to_RAS_transfo(path_reference_volume, path_affine)






