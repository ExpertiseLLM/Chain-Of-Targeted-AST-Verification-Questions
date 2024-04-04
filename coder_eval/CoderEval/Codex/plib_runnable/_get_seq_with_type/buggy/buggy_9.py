def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, (str, bytes)):
		return seq, (str, bytes)
	else:
		try:
			return _get_seq_with_type(iter(seq), bufsize)
		except TypeError:
			pass
		try:
			return _get_seq_with_type(buffer(seq), bufsize)
		except TypeError:
			pass
	return seq, None

