def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if not isinstance(obj, basestring):
		obj = str(obj)
	if isinstance(obj, unicode):
		return obj
	if isinstance(obj, bytes):
		return obj.decode('utf-8')
	return obj.encode('utf-8')

