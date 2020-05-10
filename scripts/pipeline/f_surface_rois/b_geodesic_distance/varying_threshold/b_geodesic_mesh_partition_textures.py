import os
from soma import aims, aimsalgo
import numpy as np
from variables import SUBJ_LIST, SIDES, GYRI,DIR_OUT







if __name__ == '__main__':

    SUBJ_LIST = ['114621']
    for i, subject in enumerate(SUBJ_LIST):

        for j, side in enumerate(SIDES):
            for k, gyri in enumerate(GYRI):

                partition = np.load(os.path.join(DIR_OUT,'geodesic_distances','partitions', subject + '_' + side + '_' + gyri + '.npy'))
                partition = partition.astype(np.float32)
                partition_t = aims.TimeTexture(partition)
                aims.write(partition_t, os.path.join(DIR_OUT,'geodesic_distances','partitions', subject + '_' + side + '_' + gyri + '.gii'))

















