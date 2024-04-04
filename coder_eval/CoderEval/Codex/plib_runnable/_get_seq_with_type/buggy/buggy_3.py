def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, (str, bytearray)):
		if bufsize is None:
			bufsize = len(seq)
		seq = (seq[pos:pos + bufsize] for pos in range(0, len(seq), bufsize))
		seq_type = type(seq)
	else:
		seq_type = type(seq)
		if seq_type is not type(iter(seq)):
			seq = iter(seq)
	return seq, seq_type

