import numpy as np



def select_association_streamlines_from_meshes(path_nearest_mesh_vertex, path_hemisphere_index, path_tractogram):
    nearest_mest_vertices = np.load(path_nearest_mesh_vertex)
    hemisphere_index = np.load(path_hemisphere_index)
    tractogram = np.load(path_tractogram)







if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        DWI_2_T1,
        TISSUE_MASKS,
        TRACTS,
        ASSOCIATION_TRACTS,
    )

    for subject in SUBJ_LIST:
        for side in SIDES.keys():
            select_association_streamline(
                TISSUE_MASKS[(subject, side)],
                DWI_2_T1[subject],
                TRACTS[(subject, "trk", "filtered")],
                ASSOCIATION_TRACTS[(subject, side)],
            )

#
