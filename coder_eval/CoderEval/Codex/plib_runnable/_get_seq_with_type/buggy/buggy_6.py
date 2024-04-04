def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, Sequence):
		return (seq, type(seq))
	else:
		return (list(seq), list)

