import subprocess
import xml.etree.ElementTree as ET
from libs.tools.cluster import launch_subject_cmd
from configuration.configuration import BRAINVISA, BRAINVISA_PYTHON


def modify_template_bvproc(path_template_bv_proc, old, subject, path_bvproc_subject):
    """
    Read a example bvproc and replace a pattern (old) by a new one (subject) in all
    tags. Assume that the template was done on one example subject and that only the subject id
    must be modified
    :param path_template_bv_proc: path of the example bvproc file
    :param old: pattern to be replaced (usually subject identifier)
    :param subject: new subject identifier
    :param path_bvproc_subject: path of the modified bvproc
    :return:
    """
    template_bvproc = ET.parse(path_template_bv_proc)
    template_root = template_bvproc.getroot()
    for tag in template_root.iter("*"):
        init_value = tag.text
        # sometimes tag.text is empty (None) or different type
        if type(init_value) is str:
            new_value = init_value.replace(old, subject)
            tag.text = new_value
    template_bvproc.write(path_bvproc_subject, encoding="utf-8", xml_declaration=True)
    pass


def compute_surfacic_curvature(path_mesh, path_curvature_tex, bv_instance=BRAINVISA):
    """
    :param path_mesh:
    :param path_curvature_tex:
    :return:
    """
    cmd = (
        bv_instance
        + "/bin/AimsMeshCurvature "
        + " -i "
        + path_mesh
        + " -o "
        + path_curvature_tex
        + " -m fem"
    )
    subprocess.run(cmd)
    pass


def compute_geodesic_distance(
    path_mesh, path_texture, path_distance, bv_instance=BRAINVISA
):
    """
    Wrapper for the Aims geodesic distance command
    :param path_mesh: path of the mesh
    :param path_texture: path of the object definition texture. Distance is calculated from the object
    :param path_distance: path of the geodesic distance texture
    :return: None
    """
    cmd = (
        bv_instance
        + "/bin/AimsMeshDistance"
        + " -i "
        + path_mesh
        + " -o "
        + path_distance
        + " -t "
        + path_texture
    )
    subprocess.run(cmd)
    pass


def launch_subject_bvproc(
    subject_bvproc, subject, dir_cluster, python=BRAINVISA_PYTHON, core=1
):
    """
    Launch a set of processings summed-up in a .bvproc file in a passive way in the INT cluster
    :param subject_bvproc: path to the bvproc associated to the subject
    :param subject: subject identifier (e.g. name, or HCP id)
    :param dir_cluster:
    :param python: python used to execute the bvproc (must be a Brainvisa python)
    :param core: number of cores dedicated to the processing (max 16)
    :return: None
    """

    cmd = python + " -m   brainvisa.axon.runprocess  --enabledb " + subject_bvproc
    launch_subject_cmd(cmd, subject, dir_cluster, core)
    pass
