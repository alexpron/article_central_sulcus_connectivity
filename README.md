# U-shape short-range extrinsic connectivity organisation around the human central sulcus

This repository regroups the code used to carry out the design, the magnetic resonance imaging (MRI) data processing, the statistical analyses and  figures of the study *U-shape short-range extrinsic connectivity organisation around the human central sulcus*
. A pre-print  summarizing this study is also available here: (https://www.biorxiv.org/content/10.1101/2020.05.07.082800v1)

## Dependencies
This study was performed relying on:
   1. FreeSurfer version 6 (https://surfer.nmr.mgh.harvard.edu)
   2. BrainVISA version 4.6.1 /Anatomist (http://brainvisa.info/web/index.html) 
   3. Mrtrix3 (https://www.mrtrix.org/)
   4. Ants (https://github.com/ANTsX/ANTs)
   5. COMMIT (https://github.com/daducci/COMMIT)
   6. Matplotlib 3.2 (not included into the BrainVISA 4.6.1 python environment)

## Repository organisation
This repository is structured as follows:

+ ``configuration``: 
    + ``configuration.py``: script containing global variables and data structure used in the study. These variables must be changed to adapt to your own data organisation
    + ``set_env.sh``: bash equivalent of the ``configuration.py`` python script. Must be sourced to have access to global variables
    + ``subjects_list.txt``: IDs of the HCP subjects selected in this study

+ ``libs``: modules and functions used that can be imported to reproduce the study 
+ ``scripts``: code used in this study that depend on the data structure specific to the Institut of Neurosciences (INT)
    + ``pipeline``: scripts summarizing step by step (see Pipeline below) the processing carried out
    + ``statistics``: data reformating (.csv) and statistical tests
    + ``figures``: scripts to produce main figures of the study
+ ``templates``: BrainVISA process (bvproc) template file that summarize the process used to import the FreeSurfer results into the BrainVISA ecosystem. Can be used and adapted to reproduce this step.


## Pipeline 
    
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
   6. Streamlines extremities projection
   7. Connectivity profiles
   8. Group profiles clustering     