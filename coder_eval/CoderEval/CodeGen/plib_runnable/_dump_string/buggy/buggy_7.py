def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if type(obj) == str:
		return obj.encode('utf-8')
	if type(obj) == unicode:
		return obj.encode('utf-8')
	return json.dumps(obj, cls=dumper)

