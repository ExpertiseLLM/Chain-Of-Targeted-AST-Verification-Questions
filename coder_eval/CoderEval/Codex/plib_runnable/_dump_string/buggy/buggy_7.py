def _dump_string(obj, dumper=None):
	if dumper is None:
		dumper = yaml.dump
	return dumper(obj, encoding='utf-8', allow_unicode=True, default_flow_style=False)


