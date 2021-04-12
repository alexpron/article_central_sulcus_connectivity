"""
Cleaning and parameterization of cleaned_lines living on 2D triangular meshes

author: Olivier Coulon (olivier.coulon@univ-amu.fr)

cleaned_lines generated using shortest path algorithm or manual drawing may contain loop
when converting them to texture (by default in Anatomist, two closest neighbours
of a texture are connected). Hereunder is an exemple of such a topological loop:


These module allows the user to:
+ remove most of the loops of a curve
+ parameterize a curve using normalized curvicleaned_linear abscissa

TO DO: implement a trimesh version of curve cleaning algorithm
"""


import numpy as np
from soma import aims


def clean_cleaned_line(mesh, draw):
    vert = np.array(mesh.vertex())
    neigh = aims.SurfaceManip.surfaceNeighbours(mesh)

    # extracting cleaned_lines points and detecting its extremities
    line = np.where(draw != 0)[0]
    lineNeigh = np.zeros(line.size)

    for i in range(line.size):
        v = line[i]
        lineNeigh[i] = np.where(draw[neigh[v].list()] != 0)[0].size

    # removing triangles inside the cleaned_line
    for i in range(line.size):
        v = line[i]
        other = np.where(draw[neigh[v].list()] != 0)[0]

        if other.size == 2:
            v1 = neigh[v].list()[other[0]]
            v2 = neigh[v].list()[other[1]]
            i1 = np.where(line == v1)[0]
            i2 = np.where(line == v2)[0]
            if ((lineNeigh[i] == 2) and (lineNeigh[i1] == 3) and (lineNeigh[i2] == 3)):
                draw[v] = 0

    # re-extracting line points and re-detecting extremities

    line = np.where(draw != 0)[0]
    lineNeigh = np.zeros(line.size)
    for i in range(line.size):
        v = line[i]
        lineNeigh[i] = np.where(draw[neigh[v].list()] != 0)[0].size

    extremities = np.where(lineNeigh == 1)[0]
    if extremities.size != 2:
        print('!!! Wrong number of extremities:', extremities.size)
        return np.zeros(1)  # failed !
            # to avoid this, one solution would be to take at random one of the two extremal points

    # here we determine the ventral and dorsal extremities
    if (vert[line[extremities[0]]][2] < vert[line[extremities[1]]][2]):
        iV = extremities[0]
        iD = extremities[1]
    else:
        iV = extremities[1]
        iD = extremities[0]

    vV = line[iV]  # anterior extremity
    vD = line[iD]  # posterior extremity

    # reconstructing line from ventral to dorsal extremity
    # initialisation to negative indexes (does not index any vertex of the mesh)
    cleaned_line = -1 * np.ones(line.size, dtype=int)
    cleaned_line[0] = vV
    cleaned_line[1] = neigh[vV].list()[np.where(draw[neigh[vV].list()] != 0)[0][0]]
    cleaned_line[line.size - 1] = vD
    for i in range(2, line.size-1):
        cand = np.where(draw[neigh[cleaned_line[i - 1]].list()] != 0)[0]

        if neigh[cleaned_line[i - 1]].list()[cand[0]] in cleaned_line:
            cleaned_line[i] = neigh[cleaned_line[i - 1]].list()[cand[1]]
        else:
            cleaned_line[i] = neigh[cleaned_line[i - 1]].list()[cand[0]]

    return cleaned_line



def normalized_curv_parametrisation(vertices, norm_const=100):
    """
    Compute an intrisic paramaterization of a N-D curve (a set of ordered N-D vertices)
    by curvicleaned_linear abcissa normalized to a constant (norm_const)
    param vertices: Ordered set of vertices making the cleaned_line
    type vertices: (N,D) numpy array where N is the number of vertices and D the dimension of the space
    param norm_const: chosen normalization constant (by default 100)
    return param: parameterization of the curve
    rtype: (N,) numpy array
    """
    # compute Euclidean distance between adjacent vertices composing the cleaned_line
    tmp = np.cumsum(np.sqrt(np.sum(np.diff(vertices, axis=0)**2, axis=-1)))
    # normalize to 1 by dividing by total length of the cleaned_line
    tmp /= tmp[-1]
    # multiply by chosen normalization const
    tmp *= norm_const
    # starting point (0) was removed, add it again
    param = np.zeros(len(tmp) + 1)
    param[1:] = tmp
    return param