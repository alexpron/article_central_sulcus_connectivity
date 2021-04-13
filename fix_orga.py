import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/sulci/cs/landmarks/fundus/cleaned'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*.npy'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('central_sulcus','cs')
    gf = os.path.join(dir_meshes, t)
    os.rename(f, gf)
