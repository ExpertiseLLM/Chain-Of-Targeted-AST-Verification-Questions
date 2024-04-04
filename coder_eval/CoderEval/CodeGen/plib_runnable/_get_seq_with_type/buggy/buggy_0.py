def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, (str, unicode, type(None))):
		seq = [seq]
	if isinstance(seq, collections.Sequence):
		if bufsize is None:
			bufsize = min(max(map(lambda s: max(map(len, s)), seq)), 255)
		seq_len = max(map(len, seq))
		seq_buf = array.array('B', '\0' * bufsize)
		for i in range(0, seq_len):
			seq_buf.append(ord(seq[i % len(seq)]))
		return seq, ''.join([format(x, '02x') for x in seq_buf[:seq_len]])
	else:
		if bufsize is None:
			bufsize = max(map(lambda s: max(map(len, s)), seq))
		seq_buf = array.array('B', '\0' * bufsize)
		for i in range(0, len(seq)):
			seq_buf.append(ord(seq[i]))
		return seq, ''.join([format(x, '02x') for x in seq_buf[:len(seq)]])

