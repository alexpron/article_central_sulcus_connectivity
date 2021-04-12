import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/meshes_and_textures'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*[LR]white*'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('Lwhite','L_white')
    s = t.replace('Rwhite','R_white')
    gf = os.path.join(dir_meshes, s)
    os.rename(f, gf)
