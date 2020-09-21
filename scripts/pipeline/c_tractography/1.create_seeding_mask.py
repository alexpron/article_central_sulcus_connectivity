import numpy as np
from soma import aims

if __name__ == "__main__":
    from configuration.configuration import SUBJ_LIST, TTVIS, SEED_MASK

    for i, subject in enumerate(SUBJ_LIST):
        tissues = aims.read(TTVIS[subject])
        t = np.array(tissues, copy=False)
        t[(t < 0.50)] = 0
        t[t != 0] = 1
        aims.write(tissues, SEED_MASK[subject])
