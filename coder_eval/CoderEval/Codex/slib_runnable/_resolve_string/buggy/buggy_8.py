def _resolve_string(matcher):
	name, default = matcher.group(1), matcher.group(2)
	value = os.environ.get(name)
	if value is None:
		if default is None:
			raise Error('variable %s not defined in environment' % (name))
		else:
			value = default
	return value

