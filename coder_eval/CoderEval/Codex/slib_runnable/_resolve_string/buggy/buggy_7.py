def _resolve_string(matcher):
	name, default = matcher.group('name'), matcher.group('default')
	value = os.environ.get(name)
	if value is None and default is None:
		raise Error("Environment variable {} is not defined".format(name))
	return value or default


