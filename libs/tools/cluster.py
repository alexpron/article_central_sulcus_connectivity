"""
Some Python wrapping of the frioul_batch command available on the head of the INT HPC Cluster
in order to facilitate passive/ parallel computation
"""

import os
import subprocess


def launch_cmd(cmd, core, exec_dir, stdout_file, stderr_file, cmd_file):
    """
    Basic wrapping of the frioul_batch command
    :param cmd: the whole command to be executed on the cluster
    :param core: the number of CPU core to use: between 1 to 16
    :param exec_dir: the directory where to launch the command
    :param stdout_file: the  asbolute path of the standart output file of the process
    :param stderr_file: the  asbolute path of the standart error file of the process
    :param cmd_file: the command passed to frioul_batch (should be cmd)
    :return: None
    """
    subprocess.run(
        "frioul_batch"
        + " -d "
        + exec_dir
        + " -E "
        + stderr_file
        + "  -O "
        + stdout_file
        + " -C "
        + cmd_file
        + " -c "
        + str(core)
        + ' "'
        + cmd
        + '"'
    )
    pass


def launch_subject_cmd(cmd, subject, dir_cluster, core=1):
    """
    Wrapping to lauch a command for a given HCP subject on the INT cluster using passive nodes.
    The standarts metadata files (stderr, stdout, cmd) are renamed to include subject identifier
    :param cmd:
    :param subject:
    :param dir_cluster:
    :param core:
    :return:
    """
    # creating appropriate files for cluster outputs
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)
    stderr = os.path.join(dir_cluster, subject + ".stderr")
    stdout = os.path.join(dir_cluster, subject + ".stdout")
    cmd_file = os.path.join(dir_cluster, subject + ".cmd")
    launch_cmd(cmd, core, dir_cluster, stdout, stderr, cmd_file)
    pass
