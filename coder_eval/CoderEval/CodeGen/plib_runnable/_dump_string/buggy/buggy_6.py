def _dump_string(obj, dumper=None):
	"""
	Dump to a py2-unicode or py3-string
	"""
	if dumper is None:
		dumper = MyDumper()
	return dumper.represent_string(obj)

