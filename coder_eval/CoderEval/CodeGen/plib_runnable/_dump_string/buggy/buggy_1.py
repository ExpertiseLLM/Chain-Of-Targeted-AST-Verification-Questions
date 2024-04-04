def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, str):
		return obj
	elif isinstance(obj, bytes):
		return obj.decode('utf-8')
	else:
		return str(obj).encode('utf-8')
	
