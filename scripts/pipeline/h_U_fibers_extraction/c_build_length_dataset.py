import os
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from meshes_.fibers.processing import get_lengths
from variables import SUBJ_LIST, SIDES, DIR_OUT,DIR_DATA

if __name__ == '__main__':

    path_hemispheres_index = os.path.join(DIR_OUT, 'connectivity', 'indexes', 'hemispheres_index.npy')
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index,2)
    #build side index
    hemispheres = np.zeros(side_index.shape,dtype=object)
    hemispheres[:] = 'R'
    hemispheres[side_index == 0] = 'L'

    subjects = np.array([])
    lengths = np.array([])

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            index = len(SIDES)*i + j
            path_U_fibers = os.path.join(DIR_OUT, 'U_fibers', 'arrays', subject + '_' + side +
                                         '.npy')
            streamlines = np.load(path_U_fibers)
            clust_stream = streamlines
            subjects = np.concatenate((subjects, int(subject) * np.ones(clust_stream.shape[0])))
            length = get_lengths(clust_stream)
            lengths = np.concatenate((lengths,length))
    df = pd.DataFrame({'Subject':subjects.astype(int),'Hemisphere':hemispheres,'Length':lengths})
    df.to_csv(os.path.join(DIR_OUT,'connectivity','coordinates','raw','U_fibers_length.csv'),index=False)



