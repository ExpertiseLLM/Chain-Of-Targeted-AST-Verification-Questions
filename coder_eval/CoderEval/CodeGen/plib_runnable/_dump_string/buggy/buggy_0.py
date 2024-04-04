def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, string_types):
		return obj
	if hasattr(obj, 'dump'):
		return obj.dump(dumper=dumper)
	if PY3:
		return obj.encode('utf-8')
	return obj.encode('utf-8','surrogatepass')