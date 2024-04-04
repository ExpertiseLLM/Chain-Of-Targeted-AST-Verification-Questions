def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, _seq_types):
		return (seq, type(seq))
	if hasattr(seq, '__getitem__'):
		if bufsize is None:
			return (seq, _seq_types[0])
		else:
			return (iter(seq), _seq_types[0])
	raise TypeError('invalid sequence type: %r' % type(seq))


