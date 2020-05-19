import numpy as np
from soma import aims, aimsalgo


def adaptative_distance(gyral_line, sulcal_line, mesh):
    geo = aims.GeodesicPath(mesh, 0, 0)
    indexes = np.zeros(len(gyral_line), dtype=int)
    geo_dist = np.zeros(len(gyral_line), dtype=np.float32)
    for i, g in enumerate(gyral_line):
        index, length = geo.shortestPath_1_N_ind(g, sulcal_line)
        geo_dist[i] = length
    return geo_dist


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, SIDES, MESHES, ADJACENT_GYRI, SULCUS, GYRAL_CRESTS, SULCUS_FUNDI, \
        ROI_DISTANCES

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            mesh = aims.read(MESHES[(subject, side, 'white')])
            sulcus_fundus = np.load(SULCUS_FUNDI[(subject, side, 'cleaned', 'array')])
            for k, gyrus in enumerate(ADJACENT_GYRI[SULCUS]):
                gyral_crest = np.load(GYRAL_CRESTS[(subject, side, gyrus, 'cleaned', 'array')])
                distance = adaptative_distance(gyral_crest, sulcus_fundus, mesh)
                np.save(ROI_DISTANCES[(subject, side, gyrus)], distance)
