def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher is None:
		raise ValueError("Matcher should not be None")

	elif isinstance(matcher, string_types):
		if matcher in env:
			return env[matcher]
		else:
			return None

	elif isinstance(matcher, dict):
		if not matcher:
			return None
		for key, value in matcher.iteritems():
			if key in env:
				return env[key]
			else:
				return None

	else:
		raise TypeError("Matcher should be a string or a dict")