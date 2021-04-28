import numpy as np
from soma import aims, aimsalgo



if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        MESHES,
        TRACTOGRAMS,
        NEAREST_VERTEX,
        ASSOCIATION_TRACTS
    )

    for i, subject in enumerate(SUBJ_LIST):
            l_mesh = aims.read(MESHES[subject, 'L', 'white'])
            l_s = l_mesh.size()
            r_mesh = aims.read(MESHES[subject,'R', "white"])
            r_s = r_mesh.size()
            hemi_index = np.zeros(l_s + r_s)
            hemi_index[l_s:] = 1
            aims.SurfaceManip.meshMerge(l_mesh, r_mesh)
            s_nearest = np.load(NEAREST_VERTEX[subject, 's'])
            e_nearest = np.load(NEAREST_VERTEX[subject, 'e'])
            tractogram = np.load(TRACTOGRAMS[subject])
            for j, side in enumerate(SIDES.keys()):
                association_tracts_filter = (s_nearest != e_nearest)*(hemi_index==j)
                association_tracts = tractogram[association_tracts_filter == True]
                np.save(ASSOCIATION_TRACTS[subject, side], association_tracts)










