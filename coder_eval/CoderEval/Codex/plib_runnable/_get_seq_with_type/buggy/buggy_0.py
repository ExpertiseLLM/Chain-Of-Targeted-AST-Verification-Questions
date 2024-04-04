def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, (unicode, str)):
		return (seq, unicode)
	# return (seq, type(seq))
	if isinstance(seq, (list, tuple)):
		return (seq, type(seq))
	if isinstance(seq, Buffer):
		return (seq.getvalue(), unicode)
	if hasattr(seq, 'read'):
		if bufsize is None:
			bufsize = 4096
		s = seq.read(bufsize)
		if not s:
			return (u'', unicode)
		seq.seek(-len(s), 1)
		return (s, unicode)
	if hasattr(seq, '__iter__'):
		return (seq, type(seq))
	raise TypeError(
			'argument must be a sequence or buffer object'
			)


