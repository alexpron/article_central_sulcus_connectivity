import os
import numpy as np
from skimage.feature import peak_local_max
from variables import SUBJ_LIST, SIDES, DIR_OUT



if __name__ == '__main__':

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            print subject, side
            path_density = os.path.join(DIR_OUT,'connectivity','densities','subjects','iso' + '_' + subject + '_' + side + '_' + 'filtered_radius_5.npy')
            density = np.load(path_density)
            peaks_indexes = peak_local_max(density)
            np.save(os.path.join(DIR_OUT,'connectivity','densities','subjects','local_peaks',subject + '_' + side + '.npy'),peaks_indexes)





