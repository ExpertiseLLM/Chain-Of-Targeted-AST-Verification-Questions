def _resolve_string(matcher):
	name = matcher.group(1)
	value = os.environ.get(name)
	if value is None:
		default = matcher.group(2)
		if default is not None:
			return default
		raise Error('environment variable %s not defined' % name)
	return value

