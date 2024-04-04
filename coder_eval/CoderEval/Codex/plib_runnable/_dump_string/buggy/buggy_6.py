def _dump_string(obj, dumper=None):
	if dumper is None:
		dumper = default_dumper
	return dumper(obj)


