def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if not isinstance(seq, collections.Sequence):
		raise TypeError('Expected sequence, got %s' % type(seq))
	if not seq:
		raise ValueError('Empty sequence')
	if len(seq) == 0:
		raise ValueError('Empty sequence')
	if len(seq) == 1:
		return seq, type(seq[0])
	if bufsize is None:
		bufsize = max(200, len(seq) * 4)
	buf = array.array('B', [0] * bufsize)
	#