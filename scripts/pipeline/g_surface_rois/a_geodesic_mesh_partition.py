from soma import aims, aimsalgo
import numpy as np


def partition_mesh(line, mesh, roi):
    """
    Create a partition of a mesh such as each vertex of the mesh is associated to its closest point belonging
    to a line drawn onto the mesh
    :param line: sorted np.array
    :param mesh:
    :param surf_roi:
    :return:
    """
    geo = aims.GeodesicPath(mesh, 0, 0)
    vertices = np.array(mesh.vertex())
    partition = -1 * np.ones(vertices.shape[0], dtype=int)
    if roi is not None:
        roi_indexes = np.where(roi != 0)[0].tolist()
    else:
        roi_indexes = np.arange(vertices.shape[0], dtype=int).tolist()
    for i, vertex in enumerate(roi_indexes):
        index, length = geo.shortestPath_1_N_ind(vertex, line)
        partition[vertex] = index
    return partition


if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        MESHES,
        GYRI,
        GYRAL_CRESTS,
        GEO_DISTS,
        PARTITIONS,
    )

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            mesh = aims.read(MESHES[(subject, side, "white")])
            for k, gyrus in enumerate(GYRI):
                geo_dist_tex = aims.read(GEO_DISTS[(subject, side, "white", gyrus)])
                geodesic_distance = np.array(geo_dist_tex[0])
                roi = np.zeros_like(geodesic_distance)
                roi[geodesic_distance < 30] = 1  # to reduce computation time
                gyral_line = np.load(
                    GYRAL_CRESTS[(subject, side, gyrus, "cleaned", "array")]
                )
                gyral_line = gyral_line.tolist()
                partition = partition_mesh(gyral_line, mesh, roi)
                np.save(PARTITIONS[(subject, side, gyrus, "array")], partition)
                partition_tex = aims.TimeTexture(partition)
                aims.write(partition_tex, PARTITIONS[(subject, side, gyrus, "texture")])
