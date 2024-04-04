def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, basestring):
		return seq, type(seq)
	else:
		return tuple(seq), type(seq)


