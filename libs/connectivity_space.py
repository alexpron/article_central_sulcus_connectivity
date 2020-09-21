import numpy as np
from soma import aims
from scipy.stats import gaussian_kde


def reencode_index(streamlines_mesh_index, gyrus_index):
    """
    :param streamline_mesh_index:
    :param gyrus_index:
    :return:
    """
    # to avoid conflict if mesh index is included into gyri_index
    streamlines_gyri_index = np.copy(streamlines_mesh_index)
    for i, index in enumerate(gyrus_index):
        streamlines_gyri_index[streamlines_mesh_index == index] = i
    return streamlines_gyri_index


def get_streamline_coord_on_gyri(
    s_vertex,
    e_vertex,
    precentral_vertex,
    postcentral_vertex,
    distance_precentral,
    distance_postcentral,
    mesh,
):
    # instanciating Geodesic PAth class
    g = aims.GeodesicPath(mesh, 0, 0)
    # use precomputed distance maps
    d_s_pre = distance_precentral[s_vertex]
    d_s_post = distance_postcentral[s_vertex]
    d_e_pre = distance_precentral[e_vertex]
    d_e_post = distance_postcentral[e_vertex]
    # to store the results (initialize to neg values since index are integer)
    precentral_mesh_index = -1 * np.ones(len(s_vertex))
    postcentral_mesh_index = -1 * np.ones(len(s_vertex))

    # fibers starting in the precentral and ending into postcentral
    fiber_1 = (d_s_pre < d_s_post) * (d_e_post < d_e_pre)
    # working with indices is more convenient
    a = np.where(fiber_1 == True)[0]
    # conversely
    fiber_2 = (d_s_post < d_s_pre) * (d_e_pre < d_e_post)
    b = np.where(fiber_2 == True)[0]

    # extremities corresponding to those fibers
    s_f_1 = s_vertex[fiber_1]
    e_f_1 = e_vertex[fiber_1]
    s_f_2 = s_vertex[fiber_2]
    e_f_2 = e_vertex[fiber_2]

    # print s_f_1.shape
    # print s_f_2.shape
    # print e_f_1.shape
    # print e_f_2.shape

    # use aimsMeshDistance --> more like 10000 temporary files.
    # reduce the computation time by selecting unique vertices
    pre_v = np.unique(np.concatenate((s_f_1, e_f_2))).tolist()
    pos_v = np.unique(np.concatenate((s_f_2, e_f_1))).tolist()

    for v in pre_v:
        index1, length = g.shortestPath_1_N_ind(v, precentral_vertex.tolist())
        ind1 = a[s_f_1 == v]
        precentral_mesh_index[ind1] = index1
        ind2 = b[e_f_2 == v]
        precentral_mesh_index[ind2] = index1

    for v in pos_v:
        index2, length = g.shortestPath_1_N_ind(v, postcentral_vertex.tolist())
        ind1 = a[e_f_1 == v]
        postcentral_mesh_index[ind1] = index2
        ind2 = b[s_f_2 == v]
        postcentral_mesh_index[ind2] = index2

    # rencode the index so that it correspond to the index among the gyral line not the whole wm mesh
    precentral_index = reencode_index(precentral_mesh_index, precentral_vertex.tolist())
    postcentral_index = reencode_index(
        postcentral_mesh_index, postcentral_vertex.tolist()
    )

    return precentral_index, postcentral_index


def unnormalized_kernel(points, factor=10):
    """
    Modify the behavior of the gaussian_kde object to
    enforce a fixed size kernel (spherical gaussian)
    This kernel is not normalized for the number of points
    and the unit integration over the domain so that values
    estimated are close to the initial. "Density map" or function
    estimated using this kernel can be compared between each other
    :param points: (N,D) ndarray, N the number of points and D the dimension of the space
    :return: A kernel object
    """
    kernel = gaussian_kde(points.T, bw_method=1)
    # random spherical gaussian no prior
    kernel._data_covariance = factor * np.eye(points.T.shape[0])
    kernel.covariance = kernel._data_covariance * kernel.factor ** 2
    kernel._data_inv_cov = np.linalg.inv(kernel._data_covariance)
    kernel.covariance = kernel._data_covariance * kernel.factor ** 2
    kernel.inv_cov = kernel._data_inv_cov / kernel.factor ** 2
    # kernel._norm_factor = np.sqrt(linalg.det(2*np.pi*kernel.covariance))
    kernel._norm_factor = 1
    return kernel


def estimate_pseudo_density(points, grid_size=101, factor=10):
    """
    Estimate the (unormalized connectivity_profiles with fixed kernel size)
    :param points:
    :param grid_size:
    :return:
    """
    kernel = unnormalized_kernel(points, factor)
    # creation of a grid to display the function
    x = y = np.linspace(0, 100, num=grid_size)
    X, Y = np.meshgrid(x, y)
    new_points = np.vstack([X.ravel(), Y.ravel()])
    Z = np.reshape(kernel(new_points), X.shape)
    return X, Y, Z


def compute_pseudo_density(
    path_points, path_density, grid_size=101, factor=10, path_X=None, path_Y=None
):
    points = np.load(path_points)
    X, Y, Z = estimate_pseudo_density(points, grid_size, factor)
    np.save(path_density, Z)
    if path_X is not None:
        np.save(path_X, X)
    if path_Y is not None:
        np.save(path_Y, Y)
    pass


if __name__ == "__main__":
    pass
