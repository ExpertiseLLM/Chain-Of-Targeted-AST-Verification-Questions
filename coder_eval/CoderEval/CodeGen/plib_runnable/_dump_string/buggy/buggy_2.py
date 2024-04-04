def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, bytes):
		if isinstance(obj, str):
			return obj
		else:
			return obj.decode('utf-8')
	elif isinstance(obj, string_types):
		if isinstance(obj, unicode):
			return obj
		else:
			return obj.encode('utf-8')
	elif isinstance(obj, list):
		if isinstance(obj, list):
			return [_dump_string(v, dumper=dumper) for v in obj]
		else:
			return [_dump_string(obj, dumper=dumper)]
	elif isinstance(obj, dict):
		return {_dump_string(k, dumper=dumper): _dump_string(v, dumper=dumper) for k, v in obj.items()}
	elif isinstance(obj, tuple):
		return tuple(_dump_string(i, dumper=dumper) for i in obj)
	elif isinstance(obj, frozendict):
		return {_dump_string(k, dumper=dumper): _dump_string(v, dumper=dumper) for k, v in obj.items()}
	elif isinstance(obj, set):
		return {_dump_string(k, dumper=dumper): _dump_string(v, dumper=dumper) for k, v in obj.items()}
	elif isinstance(obj, tuple):
		return tuple(_dump_string(i, dumper=dumper) for i in obj)
	elif isinstance(obj, range):
		return range(obj.start, obj.stop, obj.step)
	elif isinstance(obj, integer_types):
		return int(obj)
	elif isinstance(obj, float):
		return float(obj)
	elif isinstance(obj, complex):
		return complex(obj)
	elif isinstance(obj, (bytes, unicode)):
		return obj
	else:
		raise TypeError("Unsupported type: %s" % type(obj))

