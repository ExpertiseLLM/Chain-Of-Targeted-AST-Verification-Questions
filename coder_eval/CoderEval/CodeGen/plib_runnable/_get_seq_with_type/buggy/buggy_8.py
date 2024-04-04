def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if bufsize is None:
		bufsize = -1
	if is_sequence(seq):
		if seq[-1] is None:
			return tuple(seq[:-1]), type(seq[0])
		if not isinstance(seq[-1], type(seq[0])):
			return seq[:-1], type(seq[-1])
	return seq, type(seq)

