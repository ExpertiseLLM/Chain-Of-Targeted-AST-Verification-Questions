def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, (tuple, list)):
		return (seq, type(seq))
	if isinstance(seq, str):
		return (seq, str)
	if isinstance(seq, (bytes, bytearray)):
		return (seq, bytes)
	if isinstance(seq, memoryview):
		# Sequence is read-only
		return (seq, memoryview)
	if bufsize is not None:
		return (iter(seq), itertools.islice)
	return (iter(seq), type(seq))

