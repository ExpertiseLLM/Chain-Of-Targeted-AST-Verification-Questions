def _resolve_string(matcher):
	name, default = _split_matcher(matcher)
	try:
		return os.environ[name]
	except KeyError:
		if default is not None:
			return str(default)
		else:
			raise Error("environment variable '%s' is not defined" % name)

