import os
import pandas as pd
from variables import DIR_OUT, DIR_IN

if __name__ == '__main__':
    dir_base_tables = os.path.join(DIR_OUT, 'init_tables')
    dir_mod_tables = os.path.join(DIR_OUT, 'inter_tables')
    dir_roi_area = os.path.join(DIR_IN, 'roi_area.csv')
    # loading tables
    mesh_area = pd.read_csv(os.path.join(dir_base_tables, 'mesh_area.csv'), index_col=0)
    roi_area = pd.read_csv(os.path.join(DIR_IN, 'roi_area.csv'))
    fiedler = pd.read_csv(os.path.join(dir_base_tables, 'fiedler_length.csv'), index_col=0)
    geo_depth = pd.read_csv(os.path.join(dir_base_tables, 'geo_depth.csv'), index_col=0)
    pp = pd.read_csv(os.path.join(dir_base_tables, 'ppfm.csv'))
    subjects = pd.read_csv(os.path.join(dir_mod_tables, 'subjects_level.csv'))

    mesh_x_fiedl = pd.merge(mesh_area, fiedler, on=['Subject', 'Hemisphere'])
    mesh_x_fiedl_x_roi = pd.merge(mesh_x_fiedl, roi_area, on=['Subject', 'Hemisphere'])

    pp_x_geo = pd.merge(geo_depth, pp, on=['Subject', 'Hemisphere'])

    hemi_level = pd.merge(mesh_x_fiedl_x_roi, pp_x_geo, on=['Subject', 'Hemisphere'])

    # add subjects level informations
    whole_hemi_level = pd.merge(subjects, hemi_level, on='Subject')
    # remove index column
    whole_hemi_level = whole_hemi_level.drop(columns=['Unnamed: 0'])

    whole_hemi_level.to_csv(os.path.join(DIR_OUT, 'inter_tables', 'hemispheres_level.csv'), index=False)
