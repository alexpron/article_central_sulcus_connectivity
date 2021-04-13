import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/sulci/cs/landmarks/surf_rois/adaptive_threshold'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*.npy'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('.npy', '')
    u = t + '"dist_threshold.npy'
    gf = os.path.join(dir_meshes, u)
    os.rename(f, gf)
