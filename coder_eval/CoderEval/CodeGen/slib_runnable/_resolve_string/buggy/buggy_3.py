def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.var is None:
		raise ValueError('Variable "{}" does not exist in environment.'.format(matcher.name))
	return matcher.var

