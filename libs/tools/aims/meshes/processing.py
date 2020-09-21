"""
Generic mesh processing and conversion (essentially wrappers from Pyaims functions)
"""

from copy import copy
import numpy as np
from soma import aims


def vertices_and_faces_to_mesh(vertices, faces):
    """
    Create an aims 2D or 3D mesh using precomputed vertices and faces. Vertices and faces are assumed to be compatible
    Note this should note be used as default aims.TimeSurface() function does exactly the same things but I did not know it
    at the time
    :param vertices: ndarray
    :param faces: ndarray
    :return: AimsTimeSurface
    """
    # determine the mesh type based on polygon type (does not work for quads polygon !)
    poly_type = faces.shape[-1]
    mesh = aims.TimeSurface(dim=poly_type)
    v = mesh.vertex()
    p = mesh.polygon()
    v.assign([aims.Point3df(x) for x in vertices])
    p.assign([aims.AimsVector(x, dtype="U32", dim=poly_type) for x in faces])
    # recompute normals, not mandatory but to have coherent mesh
    # rem does not work for 2D meshes normals need to be added manually (works like a texture)
    mesh.updateNormals()
    return mesh


def mesh_2D_Merge(mesh_base, added_mesh, update_normals=True):
    """
    Merge 2d-meshes (Aims.SurfaceManip.meshMerge only handle 3D-meshes)
    The mesh_base parameter will be overwritten by the fusion (same as Aims.SurfaceManip.meshMerge)
    :param mesh_base: AimsTimeSurface_2D_VOID
    :param added_mesh: AimsTimeSurface_2D_VOID
    :return void
    """
    # Fixing sizes of the respective mesh
    # copies are mandatory due to prevent from update on the fly of objects
    s1 = copy(mesh_base.vertex().size())
    s2 = copy(added_mesh.vertex().size())
    p1 = copy(mesh_base.polygon().size())
    p2 = copy(added_mesh.polygon().size())
    # Vertices fusion
    # Allocating space for fusion
    mesh_base.vertex().resize(s1 + s2)
    mesh_base.vertex()[s1:] = added_mesh.vertex()[:]
    # Polygons fusion
    # Allocating space for fusion
    mesh_base.polygon().resize(p1 + p2)
    # Due to weird comportment of polygons, it needs to be done with for loop
    for i, p in enumerate(added_mesh.polygon()):
        p = p + s1
        mesh_base.polygon()[p1 + i] = p
    pass


def build_2D_line(n):
    """
    Build streamlines faces out of a set of n vertices assuming the mesh is a line without loop
    :param n: number of vertices (at least 2)
    :return: indices of mesh faces.
    """
    faces = np.zeros((n - 1, 2), dtype=np.int16)
    faces[:, 0] = np.arange(n - 1)
    faces[:, 1] = np.arange(1, n)
    return faces


def vertices_to_2d_line(vertices):
    """
    :param vertices: a Nx3 ndarray
    :return: mesh
    """
    if len(vertices) == 0:
        mesh = aims.TimeSurface()
    else:
        faces = build_2D_line(vertices.shape[0])
        mesh = vertices_and_faces_to_mesh(vertices, faces)
    return mesh


def indexMerge(mesh_list):
    """
    :param list of mesh to be fusionned
    :return: AimsTimeTexture
    aims.meshMerge "concatenate the two meshes", this function create an index texture
    to keep trace of origin mesh. Useful for example for left and right hemisphere
    """
    # TO DO : remplace mesh list by *args
    sizes = np.array([len(np.array(m.vertex())) for m in mesh_list], dtype=int)
    tot = np.sum(sizes)
    c = np.cumsum(sizes)
    t = np.zeros(tot)
    for i, n in enumerate(c):
        if i == 0:
            continue
        else:
            t[c[i - 1] : c[i]] = i
    texture = aims.TimeTexture(t)
    return texture


def mesh_normals_as_arrows(mesh):
    """
    Given a mesh automatically generate the normal (tangent in case of a 2D lines mesh) vertex associated
     vector field as a quiver mesh (Note: in new version of Anatomist this can be achieved be the fusion mechanism)
    :param mesh: AimsTimeSurface object
    :return:
    """
    vertices = np.array(mesh.vertex())
    normals = np.array(mesh.normal())
    start_point = vertices
    end_point = vertices + normals
    arrows = [
        aims.SurfaceGenerator.arrow(
            end_point[i].tolist(), start_point[i].tolist(), 1.1, 0.1, 4, 1
        )
        for i, s in enumerate(start_point)
    ]

    for i, arrow in enumerate(arrows):
        if i == 0:
            normals_mesh = arrow
        else:
            aims.SurfaceManip.meshMerge(normals_mesh, arrow)
        return normals_mesh
