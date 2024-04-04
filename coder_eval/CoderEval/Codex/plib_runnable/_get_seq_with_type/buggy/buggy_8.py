def _get_seq_with_type(seq, bufsize=None):
	if bufsize is None:
		bufsize = 8192
	if isinstance(seq, bytes):
		return seq, 'b'
	if isinstance(seq, bytearray):
		return seq, 'B'
	if isinstance(seq, str):
		return seq, 'u'
	if isinstance(seq, (list, tuple)):
		return seq, 'c'
	if isinstance(seq, io.RawIOBase):
		if not hasattr(seq, 'write'):
			raise TypeError("'%s' object is not writable" % type(seq).__name__)
		if bufsize < 0:
			raise ValueError("invalid buffer size")
		return seq, 'r'
	raise TypeError("'%s' object is not iterable" % type(seq).__name__)


