def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if isinstance(obj, six.string_types):
		if dumper is None:
			dumper = _py3_string_dumper
		return dumper.represent_string(obj)
	elif isinstance(obj, six.binary_type):
		if dumper is None:
			dumper = _py3_binary_dumper
		return dumper.represent_binary(obj)
	elif hasattr(obj, '__py3_proxy__'):
		return _py3_object_dumper.dump(obj.__py3_proxy__())
	else:
		raise TypeError('Unsupported type')

