from variables import  DIR_OUT, SUBJ_LIST, SIDES
from soma import aims
import numpy as np
import os




if __name__ == '__main__':

    #threshold determined previously
    threshold = 16

    for i, subject in enumerate(SUBJ_LIST):
        path_s_vertex = os.path.join(DIR_OUT,'nearest_mesh_vertex', subject + '_' + 's' +'_nearest_vertex.npy')
        path_e_vertex = os.path.join(DIR_OUT,'nearest_mesh_vertex', subject + '_' + 'e' +'_nearest_vertex.npy')
        hemi_index = np.load(os.path.join(DIR_OUT,'gw_interface', 'arrays', subject + '_hemisphere_index.npy' ))
        if os.path.exists(path_e_vertex) and os.path.exists(path_s_vertex):
            s_vertex = np.load(path_s_vertex)
            e_vertex = np.load(path_e_vertex)
            for j, side in enumerate(SIDES):

                    pre_geo_dist_tex = aims.read(os.path.join(DIR_OUT,'geodesic_distances','raw', subject + '_' +
                                                              side + '_' + 'distance_to_' + 'precentral' + '.gii'))
                    post_geo_dist_tex = aims.read(os.path.join(DIR_OUT,'geodesic_distances','raw', subject + '_' +
                                                               side + '_' + 'distance_to_' + 'postcentral' +
                                                               '.gii'))
                    pre_geo_dist = np.array(pre_geo_dist_tex[0])
                    post_geo_dist = np.array(post_geo_dist_tex[0])
                    #U shape fibers crossing condition expressed directly on geodesic distances

                    d_s_pre = pre_geo_dist[s_vertex]
                    d_s_post = post_geo_dist[s_vertex]
                    d_e_pre = pre_geo_dist[e_vertex]
                    d_e_post = post_geo_dist[e_vertex]

                    # indicate to which hemisphere belong the s and e _pointss
                    h_s = hemi_index[s_vertex]
                    h_e = hemi_index[e_vertex]

                    #First kind of crossing fibers (starting to pre-central finishing post)
                    crossing_1 = (d_s_pre<d_s_post)*(d_e_post<d_e_pre)
                    # Second kind of crossing fibers (inverse)
                    crossing_2 = (d_s_post<d_s_pre)*(d_e_pre<d_e_post)
                    #Condition about distances (inferior to threshold for both gyri)
                    d_1 = (d_s_pre <=threshold)*(d_e_post<=threshold)
                    d_2 = (d_s_post<=threshold)*(d_e_pre<=threshold)
                    #hemisphere condition (dont want interhemispheric fibers)
                    hemi = (h_s == h_e)
                    U_fibers = (crossing_1*d_1 + crossing_2*d_2) * hemi
                    #should not be necessary but juste to be sure
                    final_fibers = U_fibers * (h_s == j)

                    np.save(os.path.join(DIR_OUT, 'U_fibers', 'masks', subject + '_' + side + '_U_fibers_mask.npy'), final_fibers)



