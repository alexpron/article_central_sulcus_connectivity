import numpy as np
from scipy.stats import gaussian_kde

def unnormalized_kernel(points,factor=10):
    '''
    Modify the behavior of the gaussian_kde object to
    enforce a fixed size kernel (spherical gaussian)
    This kernel is not normalized for the number of points
    and the unit integration over the domain so that values
    estimated are close to the initial. "Density map" or function
    estimated using this kernel can be compared between each other
    :param points: (N,D) ndarray, N the number of points and D the dimension of the space
    :return: A kernel object
    '''
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
    '''
    Estimate the (unormalized density with fixed kernel size)
    :param points:
    :param grid_size:
    :return:
    '''
    kernel = unnormalized_kernel(points,factor)
    #creation of a grid to display the function
    x = y = np.linspace(0, 100, num=grid_size)
    X, Y = np.meshgrid(x, y)
    new_points = np.vstack([X.ravel(), Y.ravel()])
    Z = np.reshape(kernel(new_points), X.shape)
    return X, Y, Z

def compute_pseudo_density(path_points, path_density, grid_size=101, factor=10,path_X=None, path_Y=None):
    points = np.load(path_points)
    X, Y, Z = estimate_pseudo_density(points, grid_size, factor)
    np.save(path_density, Z)
    if path_X is not None:
        np.save(path_X, X)
    if path_Y is not None:
        np.save(path_Y, Y)
    pass



if __name__ == '__main__':
    pass