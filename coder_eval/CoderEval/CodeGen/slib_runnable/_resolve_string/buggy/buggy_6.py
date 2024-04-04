def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	var = matcher.group(1)
	default = matcher.group(2)
	if var in os.environ:
		value = os.environ[var]
		if value is None:
			raise Error("Variable '%s' not set in environment." % var)
		else:
			return value
	else:
		if default is not None:
			value = default
			if value is None:
				raise Error("Variable '%s' not set in environment." % var)
			else:
				return value
		else:
			raise Error("Variable '%s' not set in environment." % var)

