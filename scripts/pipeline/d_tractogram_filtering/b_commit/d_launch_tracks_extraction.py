import os
from libs.tractogram_filtering.sub_tracks import extract_sub_tractogram

if __name__ == '__main__':
    from configuration.configuration import SUBJ_LIST, TRACTS, COMMIT_WEIGHTS

    for subject in SUBJ_LIST:
        if os.path.exists(TRACTS[(subject, 'trk', 'raw')]) and os.path.exists(
                COMMIT_WEIGHTS[subject]) and not os.path.exists(TRACTS[(subject, 'trk', 'filtered')]):
            extract_sub_tractogram(TRACTS[(subject, 'trk', 'raw')], COMMIT_WEIGHTS[subject],
                                   TRACTS[(subject, 'trk', 'filtered')])
    pass
