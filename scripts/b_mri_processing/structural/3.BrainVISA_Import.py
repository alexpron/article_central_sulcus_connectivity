import os
import numpy as np



if __name__ == '__main__':

    #from tools import subjects_list, modify_template_bvproc, launch_subject_bvproc, is_executable_bvproc
    #Instanciating meta-variables retrieved from bash environnement
    dir_templates = os.environ["DIR_BVPROC_TEMPLATES"]
    sequence = 'import_T1_from_freesurfer'
    path_template = os.path.join(dir_templates, sequence + '.bvproc')

    dir_bvproc = os.path.join(os.environ["DIR_BVPROC"], sequence)
    dir_cluster = os.path.join(os.environ["DIR_CLUSTER"], sequence)

    #create
    if not os.path.exists(dir_bvproc):
        os.makedirs(dir_bvproc)
    #the pattern (subject_test id to replace in the bvproc#

    subject_test = os.environ["SUBJECT_TEST"]
    subjects_list = read_subjects_list(os.environ["SUBJ_LIST"])

    for i, sub in enumerate(subjects_list[:-1]):
        path_bvproc_subject = os.path.join(dir_bvproc, sub + '.bvproc')
        # #create a new bvproc corresponding to the processed subject
        modify_template_bvproc(path_template,subject_test,sub, path_bvproc_subject)
        #check if the bvproc can be executed on the cluster (when several steps are passive
        #output files may not exist
        launch_subject_bvproc(path_bvproc_subject,sub,dir_cluster, core=1)




