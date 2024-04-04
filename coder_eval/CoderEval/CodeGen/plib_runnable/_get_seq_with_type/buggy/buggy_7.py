def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if bufsize is None:
		bufsize = max(16384, len(seq) * 16)
	seq = str(seq)
	seq = seq.encode('utf-8','replace')
	seq = seq.replace('\n', '')
	seq = seq.replace('\r', '')
	if len(seq) % 16:
		seq = seq +'' * (16 - (len(seq) % 16))
	return seq, 'text'