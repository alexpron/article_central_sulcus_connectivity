import sys
import numpy as np
import nibabel as nib


def extract_sub_tractogram(path_trk, path_results, path_trk_filtered):
	'''
	:param path_trk:
	:param path_results:
	:param path_trk_filtered:
	:return: void
	'''
	trkfile = nib.streamlines.load(path_trk)
	tractogram = trkfile.tractogram
	h = trkfile.header
	#modifying
	streamlines = tractogram.streamlines
	p = np.load(path_results)
	w = p[1]
	w = w[:len(streamlines)]
	index = np.where(w>0)[0]
	sub_streamlines = [streamlines[i] for i in index]
	#modifying the length field into the header
	h['nb_streamlines'] = len(index)
	new_tractogram = nib.streamlines.Tractogram(sub_streamlines,affine_to_rasmm=np.eye(4))
	new_trk = nib.streamlines.TrkFile(new_tractogram, header=h)
	nib.streamlines.save(new_trk, path_trk_filtered)
	pass



if __name__ == '__main__':
	args = sys.argv
	path_trk_in = args[1]
	path_results = args[2]
	path_trk_out = args[3]
	extract_sub_tractogram(path_trk_in, path_results, path_trk_out)







