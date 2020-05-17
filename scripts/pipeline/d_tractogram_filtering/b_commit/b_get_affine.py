from libs.tools.aims.volume import get_aims_to_RAS_transfo
from configuration.configuration import FODS, AIMS_TO_RAS


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST
    for subject in SUBJ_LIST:
        get_aims_to_RAS_transfo(FODS[subject], AIMS_TO_RAS[subject])