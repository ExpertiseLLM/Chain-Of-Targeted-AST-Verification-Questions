def _dump_string(obj, dumper=None):
	if isinstance(obj, str):
		return obj
	else:
		return obj.encode('utf-8')

