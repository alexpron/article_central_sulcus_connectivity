import subprocess

def distance_map_to_gyrus(path_mesh, path_gyral_line, path_distance_map, ):
    cmd = '/hpc/soft/brainvisa/brainvisa_4.6.0/bin/AimsMeshDistance' + ' -i ' + path_mesh + ' -t ' + path_gyral_line + ' -o ' + path_distance_map
    subprocess.run(cmd)
    pass


if __name__ == "__main__":

    from configuration.configuration import (
        SUBJ_LIST,
        SIDES,
        MESHES,
        GYRI,
        GYRAL_CRESTS,
        GEO_DISTS,
    )

    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            for k, gyrus in enumerate(GYRI):
                distance_map_to_gyrus(MESHES[subject, side, 'white'], GYRAL_CRESTS[subject, side, gyrus,'texture'], GEO_DISTS[(subject, side, "white", gyrus)])

