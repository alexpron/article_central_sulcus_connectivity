# U-shape short-range extrinsic connectivity organisation around the human central sulcus

This repository regroups the code used to carry out the design, the magnetic resonance imaging (MRI) data processing, the statistical analyses and  figures of the study *U-shape short-range extrinsic connectivity organisation around the human central sulcus*
. A [preprint](https://www.biorxiv.org/content/10.1101/2020.05.07.082800v1) of this study is also available (see Material and Methods)

## Dependencies
This study was performed relying on :
   1. FreeSurfer version 6 (https://surfer.nmr.mgh.harvard.edu)
   2. BrainVISA version 4.6.1 /Anatomist (http://brainvisa.info/web/index.html) 
   3. Mrtrix3 (https://www.mrtrix.org/)
   4. Ants (https://github.com/ANTsX/ANTs)
   5. COMMIT (https://github.com/daducci/COMMIT)
   6. Matplotlib 3.2 (not included into the BrainVISA 4.6.1 python environnement)
    

## Repository organisation
This repository is structured as follows:

+ configuration: 
    + configuration.py: script containing global variables and data structure used in the study. These variables must be changed to adapt to your own data organisation
    + set_env.sh: bash equivalent of configuration.py script. Must be sourced to have access to global variables
    + subjects_list.txt: IDs of the HCP subjects selected in this study

+ libs: modules and functions used that can be imported to reproduce the study 
+ scripts: code used in this study  that takes into account the data and software context in the Institut of Neurosciences (INT)
context.
    + pipeline: 
    + statistics: data reformating (.csv) and statistical tests
    + figures: scripts to help to the generation or to generate figures of the study.
+ templates: brainvisa process (bvproc) template file that sum-up the process used to import the FreeSurfer results into the BrainVISA ecosystem. Can be used and adapted to reproduce the import and processing.

 
##Pipeline 
    
   1. Subjects selection 
   2. Structural (T1, T2) and diffusion weighted MRI (dMRI) processing:
        1. Tissue segmentation (FreeSurfer)
        2. Triangular meshes generation (BrainVISA)
        3. Surface maps computation (e.g. curvature, geodesic depth) (BrainVISA)
        4. dMRI volume bias correction (Ants)
        5. Multi-Shell Multi Tissue Spherical Deconvolution (Mrtrix)
   3. Whole brain anatomically constrained probabilistic tractography (Mrtrix)
   4. Tractogram filtering
        1. Filtering with respect to the dMRI signal (COMMIT)
        2. Association streamlines extraction
        3. White mesh based filtering
   5. Surface landmarks drawing
        1. Central sulcus extremities
        2. Central sulcus fundus
        3. Adjacent gyral crests
        4. Pli de passage fronto parietal moyen (PPFM) position along the fundus line and projection along the gyral crest lines
        