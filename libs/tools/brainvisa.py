import subprocess
import xml.etree.ElementTree as ET
from configuration.configuration import BRAINVISA


def modify_template_bvproc(path_template_bv_proc, old, subject, path_bvproc_subject):
    '''
    Read a example bvproc and replace a pattern (old) by a new one (subject) in all
    tags. Assume that the template was done on one example subject and that only the subject id
    must be modified
    :param path_template_bv_proc: path of the example bvproc file
    :param old: pattern to be replaced (usually subject identifier)
    :param subject: new subject identifier
    :param path_bvproc_subject: path of the modified bvproc
    :return:
    '''
    template_bvproc = ET.parse(path_template_bv_proc)
    template_root = template_bvproc.getroot()
    for tag in template_root.iter('*'):
        #print tag.text
        init_value = tag.text
        #sometimes tag.text is empty (None) or different type
        if type(init_value) is str:
            new_value = init_value.replace(old, subject)
            tag.text = new_value
    template_bvproc.write(path_bvproc_subject, encoding='utf-8', xml_declaration=True)
    pass


def compute_surfacic_curvature(path_mesh, path_curvature_tex, bv_instance=BRAINVISA):
    """
    :param path_mesh:
    :param path_curvature_tex:
    :return:
    """
    cmd = bv_instance + '/bin/AimsMeshCurvature ' + ' -i ' + path_mesh + ' -o ' + path_curvature_tex + ' -m fem'
    subprocess.run(cmd)
    pass