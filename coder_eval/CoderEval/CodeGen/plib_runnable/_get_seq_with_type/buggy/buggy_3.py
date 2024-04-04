def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if seq:
		if not isinstance(seq, Sequence):
			seq = Sequence(seq)
	else:
		seq = Sequence()
	if isinstance(seq, Seq):
		if seq.typedefs:
			seq.typedefs.sort()
		if bufsize is None:
			if len(seq.typedefs) > 1:
				bufsize = len(seq.typedefs)
				if bufsize < 1:
					bufsize = 1
			else:
				bufsize = 1
		if bufsize < 1:
			bufsize = 1
	elif isinstance(seq, str):
		if bufsize is None:
			bufsize = len(seq)
		seq = Sequence(seq)
		seq.typedefs = []
		seq.typedefs.append(seq.typedefs[-1])
	elif isinstance(seq, Sequence):
		if len(seq.typedefs) > 1:
			seq.typedefs.sort()
		if bufsize is None:
			bufsize = len(seq.typedefs)
			if bufsize < 1:
				bufsize = 1
		seq.typedefs.append(seq.typedefs[-1])
	return (seq, type(seq))

