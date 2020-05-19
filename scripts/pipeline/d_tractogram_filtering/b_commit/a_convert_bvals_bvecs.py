from libs.tractogram_filtering.commit import dipy_to_commit
from configuration.configuration import SUBJ_LIST, BVALS, BVECS, COMMIT_META

if __name__ == '__main__':

    for subject in SUBJ_LIST:
        dipy_to_commit(BVALS[subject], BVECS[subject], COMMIT_META[subject], complete_scheme=False)
