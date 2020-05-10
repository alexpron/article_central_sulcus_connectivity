import os
# from soma import aims
import numpy as np
import pandas as pd
from variables import DIR_OUT, SUBJ_LIST, SIDES, GYRI

def rescaling_handknob(gyri_parametrisation, hknob, mean_hknob):
    '''
    Piecwise affine reparameterisation of the
    :param gyri_parametrisation: intial b_coordinates of the fibers o the gyri
    :param hknob: Hand knob b_coordinates (N,2)
    :param mean_hknob: Mean of the knob array (1,2) dndrray
    :return:  N,2
    '''
    new_param = gyri_parametrisation.copy()
    new_param[new_param <= hknob] *= mean_hknob/hknob
    new_param[gyri_parametrisation>hknob] *= ((100.0 - mean_hknob)/(100.0 - hknob))
    new_param[gyri_parametrisation > hknob] += 100.0*((mean_hknob - hknob)/(100.0 - hknob))
    return new_param



if __name__ =='__main__':


   path_pp_coord_in = os.path.join(DIR_OUT,'drawing', 'ppfm','tables', 'pp_manual_drawing_coord_gyri.csv')
   path_pp_coord_out = os.path.join(DIR_OUT,'drawing', 'ppfm','tables','pp_gyri.csv')
   df = pd.read_csv(path_pp_coord_in)
   #initialisation to negative values to be sure code does something
   df['PP_Pre_Coord_Global_Mean'] = -1
   df['PP_Pre_Coord_Mean_by_Hemi'] = -1
   df['PP_Post_Coord_Global_Mean'] = -1
   df['PP_Post_Coord_Mean_by_Hemi'] = -1

   #computing means by gyrus (global mean)
   df['PP_Pre_Coord_Global_Mean'] = df['PP_Pre_Coord_Iso'].mean()
   df['PP_Post_Coord_Global_Mean'] = df['PP_Post_Coord_Iso'].mean()
   #computing means by gyrus and hemi
   df['PP_Pre_Coord_Mean_by_Hemi'] = df.groupby('Hemisphere')['PP_Pre_Coord_Iso'].transform('mean')
   df['PP_Post_Coord_Mean_by_Hemi'] = df.groupby('Hemisphere')['PP_Post_Coord_Iso'].transform('mean')
   #save the results to csv file
   df.to_csv(path_pp_coord_out,index=False)

   means = ['Global_Mean','Mean_by_Hemi']


   #starting reparametrisation(s)

   # for i, subject in enumerate(SUBJ_LIST):
   #     for j, side in enumerate(SIDES):
   #         for k, g in enumerate(GYRI):
   #
   #             path_iso_param_tex = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                           '_' + 'iso_param.gii')
   #             path_iso_param = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                           '_' + 'iso_param.npy')
   #             iso_param_tex = aims.read(path_iso_param_tex)
   #             iso_param = np.array(iso_param_tex[0])
   #             np.save(path_iso_param, iso_param)
   #
   #             var = g.replace('central','')
   #             var = var.upper()[0] + var[1:]
   #             iso_var = 'PP' + '_' + var + '_' + 'Coord_Iso'
   #             pp_iso_coord = df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere'] == side) , iso_var ]
   #
   #             pp_iso_coord = float(pp_iso_coord)
   #
   #
   #             for l, m in enumerate(means):
   #                 m_var = 'PP' + '_'  + var + '_' + 'Coord' + '_' + m
   #                 mean_pp = df.loc[(df['Subject'] == int(subject)) & (df['Hemisphere']==side) ,
   #                                m_var ]
   #                 mean_pp = float(mean_pp)
   #                 new_param = rescaling_handknob(iso_param, pp_iso_coord, mean_pp)
   #                 new_param_tex = aims.TimeTexture(new_param)
   #                 if l == 0:
   #                     path_new_param = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                           '_' + 'global_mean_param.npy')
   #                     path_new_param_tex = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                           '_' + 'global_mean_param.gii')
   #                 else:
   #                     path_new_param = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                                   '_' + 'mean_by_hemi_param.npy')
   #                     path_new_param_tex = os.path.join(DIR_OUT, 'gyral_crests', subject + '_' + side + '_' + g +
   #                                                       '_' + 'mean_by_hemi_param.gii')
   #
   #                 np.save(path_new_param,new_param)
   #                 aims.write(new_param_tex, path_new_param_tex)














































