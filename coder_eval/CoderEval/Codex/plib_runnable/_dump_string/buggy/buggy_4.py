def _dump_string(obj, dumper=None):
	dumper = dumper or json.dumps
	return dumper(obj, ensure_ascii=False, separators=(',', ':'))


