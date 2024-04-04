def _get_seq_with_type(seq, bufsize=None):
	if bufsize is None:
		bufsize = _default_bufsize
	if isinstance(seq, basestring):
		if len(seq) == 1:
			# Treat single characters as a string
			return (seq, str)
		# Multi-character strings are treated as sequences
		return (seq, (str, unicode))
	try:
		# Try to get an iterator
		iter(seq)
	except TypeError:
		# Not iterable, so treat as a single item
		return (seq, object)
	else:
		return (seq, (str, unicode))

