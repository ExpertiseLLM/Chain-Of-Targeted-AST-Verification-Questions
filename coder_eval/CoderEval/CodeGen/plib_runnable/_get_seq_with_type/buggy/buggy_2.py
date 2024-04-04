def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if bufsize is None:
		if isinstance(seq, str):
			bufsize = len(seq)
		else:
			bufsize = _default_bufsize
	t = type(seq)
	if t in (list, tuple):
		return seq, t
	elif t in (dict, _OrderedDict):
		return seq, t
	elif hasattr(seq, 'keys'):
		return seq, list
	else:
		return seq, _type_check(t, seq)

