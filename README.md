# U-shape short-range extrinsic connectivity organisation around the human central sulcus

This repository regroups the code used to carry out the design, the magnetic resonance imaging (MRI) data processing, the statistical analyses and  figures of the study *U-shape short-range extrinsic connectivity organisation around the human central sulcus*
. A [preprint](https://www.biorxiv.org/content/10.1101/2020.05.07.082800v1) of this study is also available. 

This repository is organized as follows:

+ configuration: 
    + configuration.py: script containing global variables and data structure used in the study. These variables must be changed to adapt to your own data organisation
    + set_env.sh: bash equivalent of configuration.py script. Must be sourced to have access to global variables
    + subjects_list.txt: IDs of the HCP subjects selected in this study

+ libs: modules and functions used that can be imported to reproduce the study 
+ scripts: code used in this study that takes into account the data and software context in the Institut of Neurosciences (INT)
context. This includes:
    1. Subjects selection 
    2. Structural (T1, T2) and diffusion weighted MRI (dMRI) processing:
        1. Tissue segmentation (FreeSurfer 6.0.0)
        2. Triangular meshes generation (BrainVISA)
        3. Surface maps computation (e.g. curvature, geodesic depth) (Cortical Surface toolbox)
        4. dMRI volume bias correction (Ants)
        5. Multi-Shell Multi Tissue Spherical Deconvolution (Mrtrix)
    3. Whole brain anatomically constrained probabilistic tractography (Mrtrix)
    4. Tractogram filtering
        1. COMMIT 
        2. Association streamlines extraction
        3. White mesh based filtering
        