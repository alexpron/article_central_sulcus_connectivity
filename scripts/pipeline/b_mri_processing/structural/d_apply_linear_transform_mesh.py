from soma import aims

def mesh_transform(path_mesh, path_transfo, path_mesh_out):
    transfo = aims.read(path_transfo)
    mesh = aims.read(path_mesh)
    h = mesh.header()
    aims.SurfaceManip.meshTransform(mesh,transfo)
    aims.write(mesh, path_mesh_out)
    pass


if __name__ == '__main__':

    from configuration.configuration import SUBJ_LIST, MESHES_TYPE, SIDES, T1_2_DWI, MESHES_BRAINVISA

    for i, subject in enumerate(SUBJ_LIST):
            for mesh_type in MESHES_TYPE:
                for side in SIDES.keys():
                        mesh_transform(MESHES_BRAINVISA[(subject, side, mesh_type,'t1')], T1_2_DWI, MESHES_BRAINVISA[(subject, side, mesh_type,'dwi')])


