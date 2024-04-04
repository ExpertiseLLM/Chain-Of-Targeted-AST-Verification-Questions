def _dump_string(obj, dumper=None):
	""" Dump to a py2-unicode or py3-string """

	if dumper is None:
		dumper = _dumper

	return dumper(obj).encode('utf-8')

