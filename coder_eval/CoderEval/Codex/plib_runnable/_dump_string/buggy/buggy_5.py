def _dump_string(obj, dumper=None):
	if dumper is None:
		dumper = YAMLDumper()
	return dumper.dump(obj)


