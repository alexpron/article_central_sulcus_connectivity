import numpy as np
from soma import aims

if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        GYRI,
        MESHES,
        GYRAL_CRESTS,
        GEO_DISTS,
        PARTITIONS,
        ADJ_GYRI_ROI,
        ROI_DISTANCES,
    )

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            mesh = aims.read(MESHES[(subject, side, "white")])
            for k, gyrus in enumerate(GYRI):
                # Gyral line indexes
                gyral_line = np.load(GYRAL_CRESTS[(subject, side,gyrus, "cleaned", "array")])
                gyral_line = gyral_line.tolist()
                # Geodesic distance map
                geo_dist_t = aims.read(GEO_DISTS[(subject, side, "white", gyrus)])
                geo_dist = np.array(geo_dist_t[0])
                # Mesh partitionned by geodesic distance
                partition = np.load(PARTITIONS[(subject, side, gyrus, "array")])
                # Varying distance threshold
                dist_threshold = np.load(ROI_DISTANCES[(subject, side, gyrus)])
                # Output texture
                roi = np.zeros(len(geo_dist), dtype=np.uint32)
                for l, g in enumerate(gyral_line):
                    roi[(partition == g) * (geo_dist <= dist_threshold[l])] = 1
                roi_t = aims.TimeTexture(roi)
                aims.write(roi_t, ADJ_GYRI_ROI[(subject, side, gyrus)])
