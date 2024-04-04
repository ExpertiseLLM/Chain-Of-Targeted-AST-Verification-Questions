def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group(1)
	value = matcher.group(2)
	if name in os.environ:
		return os.environ[name]
	elif value:
		return value
	else:
		raise EnvironmentError('{} not found in environment.'.format(name))