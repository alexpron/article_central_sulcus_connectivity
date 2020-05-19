"""
Compute Depth-Potential Function (DPF) maps from the BrainVISA python interface
(more convenient) than command wrapping and direct python interface because it allows
to use default set process values.
"""
import brainvisa.axon as axon
import brainvisa.processes
from configuration.configuration import SUBJ_LIST, SIDES, MESHES, DPFS

if __name__ == '__main__':

    # launch BrainVisa
    axon.initializeProcesses()
    context = brainvisa.processes.defaultContext()
    for i, subject in enumerate(SUBJ_LIST):
        for j, side in enumerate(SIDES):
            context.runProcess('Depth Potential Function', input_mesh=MESHES[(subject, side, 'white')],
                               DPF_texture=DPFS[(subject, side, 'white')])
            pass
    axon.cleanup()
