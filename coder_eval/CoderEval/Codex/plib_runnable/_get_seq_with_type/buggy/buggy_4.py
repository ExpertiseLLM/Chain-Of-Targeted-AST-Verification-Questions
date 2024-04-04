def _get_seq_with_type(seq, bufsize=None):
	if isinstance(seq, basestring):
		return (seq, 's')
	try:
		t = type(seq)
		return (t(seq), 'm')
	except TypeError:
		pass
	try:
		return (iter(seq), 'i')
	except TypeError:
		pass
	if bufsize is None:
		bufsize = len(seq)
	return (array('b', seq), 'b')


