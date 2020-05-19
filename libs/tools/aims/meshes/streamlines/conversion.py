import numpy as np
from soma import aims
from libs.tools.aims.meshes.processing import build_2D_line, vertices_and_faces_to_mesh, mesh_2D_Merge
from libs.tools.aims.meshes.streamlines.processing import compute_frenet_serret


def set_local_orientation(mesh, local_orientation, norm='default'):
    """Add local information orientation at vertex level (or streamline level)
    to be used in Anatomist for coloring the streamlines.
    :param mesh : AimsTimeSurface containing n vertices
    :param local_orientation : a Nx3 array containing local orientation infornation (e.g normal or tangent)
    """
    # normalizing data using default 2-norm
    # norm = np.linalg.norm(local_orientation,axis=1)
    # build our own norm 2 function
    norm = np.sqrt(np.sum(local_orientation ** 2, axis=1))
    # depending on the version of numpy it might not be accurate to use this function
    local_orientation[norm != 0] /= norm[norm != 0][:, np.newaxis]
    mesh.normal().assign(local_orientation)
    pass


def bundle_to_mesh(bundle, coloring='global'):
    """
    :param bundle: set of streamlines
    :return: mesh
    """
    if len(bundle) == 0:
        mesh = aims.TimeSurface()
    else:
        for i, s in enumerate(bundle):
            faces = build_2D_line(len(s))
            streamline = vertices_and_faces_to_mesh(s, faces)
            if i == 0:
                mesh = streamline
            else:
                mesh_2D_Merge(mesh, streamline)
        if coloring is not None:
            if coloring == 'global':
                T, N, B, k, t = compute_frenet_serret(bundle, local=False)
                del N, B, k, t
            else:
                T, N, B, k, t = compute_frenet_serret(bundle, local=True)
                del N, B, k, t
            set_local_orientation(mesh, T)
    return mesh
