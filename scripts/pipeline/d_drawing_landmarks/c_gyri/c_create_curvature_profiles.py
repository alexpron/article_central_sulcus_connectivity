import os
import numpy as np
from soma import aims
from configuration import DIR_IN, DIR_OUT, SUBJ_LIST, SIDES, MESH





if __name__ == '__main__':



    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for
            depth_t = aims.read(os.path.join(DIR_OUT, 'gyri', subject + '_' + side + '_' + gyrus + '_' +
                                                     'curvature.gii'))
            depth = np.array(depth_t[0])
            fundus = np.load(os.path.join(DIR_OUT,'sulci','fundus', sub + '_' + side + '_' + 'central_sulcus.npy'))
            depth_profile = depth[fundus]
            np.save(os.path.join(DIR_OUT,'sulci','depth_profile', sub + '_' + side + '_' + 'central_sulcus_depth.npy'),
                     depth_profile)
            # depth_profile_tex = aims.TimeTexture(depth_profile.astype(np.float32))
            # aims.write(depth_profile_tex, os.path.join(DIR_OUT,'sulci','depth_profile', sub + '_' + side + '_' +
            #                                            'central_sulcus_depth.gii'))











