def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, text_type):
		return obj.encode('utf-8')
	else:
		return obj

