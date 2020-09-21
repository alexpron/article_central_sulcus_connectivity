import os

if __name__ == "__main__":

    from libs.tools.cluster import launch_subject_cmd
    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        DIR_PROJECT,
        DIR_CLUSTER,
        ASSOCIATION_TRACTS,
        ASSO_TRACT_EXTREMITIES,
    )

    dir_cluster = os.path.join(DIR_CLUSTER, "extremities")
    if not os.path.exists(dir_cluster):
        os.makedirs(dir_cluster)

    for subject in SUBJ_LIST:
        for side in SIDES.keys():
            # TODO : Find a way to have relative path
            cmd = (
                os.path.join(
                    DIR_PROJECT,
                    "scripts",
                    "pipeline",
                    "d_extract_fibers_extremities",
                    "extract_streamlines_extremities_cluster.py",
                )
                + "  "
                + ASSOCIATION_TRACTS[(subject, side)]
                + "  "
                + ASSO_TRACT_EXTREMITIES[(subject, side, "s")]
                + "  "
                + ASSO_TRACT_EXTREMITIES[(subject, side, "e")]
            )
            launch_subject_cmd(cmd, subject, dir_cluster)
