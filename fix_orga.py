import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/sulci/cs/landmarks/adjacent_gyri/raw'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*.gii'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('.tex','')
    gf = os.path.join(dir_meshes, t)
    os.rename(f, gf)
