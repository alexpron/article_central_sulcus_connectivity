import os
import glob


dir_meshes = '/hpc/meca/users/pron.a/data/U_Fibers/sulci/cs/landmarks/extremities'
wrong_typo_files = glob.glob(os.path.join(dir_meshes, '*.gii'))
for f in wrong_typo_files:
    filename = os.path.basename(f)
    t = filename.replace('central_sulcus','cs')
    u = t.replace('_drawn.tex','')
    gf = os.path.join(dir_meshes, u)
    os.rename(f, gf)
