import numpy as np
import pandas as pd



if __name__ == '__main__':

    d = 'global_mean'
    path_coords_aligned = os.path.join(DIR_CON,'data','output','connectivity','coordinates','length_filtered',
                                'U_fibers_coord_global_mean.npy')
    path_coords_iso = os.path.join(DIR_CON, 'data', 'output', 'connectivity', 'coordinates', 'length_filtered',
                               'U_fibers_coord_iso.npy')
    path_hemispheres_index = os.path.join(DIR_CON,'data','output','connectivity','indexes',
                                          'hemispheres_index_filtered.npy')
    coords_aligned = np.load(path_coords_aligned)
    coords_iso = np.load(path_coords_iso)
    labels = np.zeros(len(coords_aligned),dtype=int)
    subjects = np.zeros(len(coords_aligned),dtype=int)
    hemispheres_index = np.load(path_hemispheres_index)
    side_index = np.mod(hemispheres_index, 2)
    #recontruct both hemispheres labels
    for j, side in enumerate(SIDES):
        path_hemi_labels  = os.path.join(DIR_CON,'data','output','group_clustering','dbscan_fixed', d + '_' + \
                                                                                                'all_labels' + '_' + \
                                                                            side + '.npy')
        hemi_labels = np.load(path_hemi_labels)
        labels[side_index==j] =  hemi_labels
    #get subjects id array from index
    sub = np.array(SUBJ_LIST,dtype=int)
    subjects = sub [((hemispheres_index - side_index)/len(SIDES)).astype(int)]

    hemispheres = np.zeros(side_index.size,dtype=object)
    hemispheres[:]= 'L'
    hemispheres[side_index == 1] = 'R'


    df = pd.DataFrame({'Subject':subjects,'Hemisphere': hemispheres ,
                       'Pre_Coord_Iso':coords_iso[:,0], 'Post_Coord_Iso':coords_iso[:,1],
                                                                         'Pre_Coord_Aligned':coords_aligned[:,0] ,
                       'Post_Coord_Aligned':coords_aligned[:,1],'Label':labels})
    df.to_csv(os.path.join(DIR_OUT,'init_tables','coordinates.csv'))










