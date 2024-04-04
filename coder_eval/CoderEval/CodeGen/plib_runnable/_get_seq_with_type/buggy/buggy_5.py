def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, str):
		seq = seq.split()
	if bufsize is None:
		bufsize = DEFAULT_BUFFER_SIZE
	buf = _empty_buf(bufsize)
	while True:
		r = seq.pop(0)
		if not r or r == '*':
			break
		if not buf:
			if isinstance(r, str):
				r = r.split()
			if len(r) == 1:
				r = r[0]
			if isinstance(r, basestring):
				buf.write(r)
			else:
				buf.write(str(r))
		else:
			if isinstance(r, str):
				r = r.split()
			if len(r) == 1:
				r = r[0]
			if isinstance(r, basestring):
				buf.write(r)
			else:
				buf.write(str(r))
	if buf:
		buf.write('\n')
	return buf.getvalue()

