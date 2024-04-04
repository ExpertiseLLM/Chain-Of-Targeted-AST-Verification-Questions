def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.name in os.environ:
		value = os.environ[matcher.name]
	elif not matcher.default is None:
		value = matcher.default
	else:
		raise Error("Variable '%s' not defined in environment" % matcher.name)
	return value