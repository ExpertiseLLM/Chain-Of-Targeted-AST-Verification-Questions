def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, unicode):
		return obj.encode('ascii')
	else:
		return obj

