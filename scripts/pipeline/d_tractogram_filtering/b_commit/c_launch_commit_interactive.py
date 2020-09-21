import os
from libs.tractogram_filtering.commit import commit_filtering

if __name__ == "__main__":

    from configuration.configuration import SUBJ_LIST, TRACTS, COMMIT_WEIGHTS

    for i, subject in enumerate(SUBJ_LIST):
        if os.path.exists(TRACTS[(subject, "trk", "raw")]) and not os.path.exists(
            COMMIT_WEIGHTS[subject]
        ):
            commit_filtering(subject)
