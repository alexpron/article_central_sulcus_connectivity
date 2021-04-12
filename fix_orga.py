import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/meshes_and_textures'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*DPF*'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('DPF','dpf')
    gf = os.path.join(dir_meshes, t)
    os.rename(f, gf)
