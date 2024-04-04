def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group(1)
	env = get_environment_variable(name)
	if env is not None:
		return env.get(name, matcher.group(2))
	else:
		raise ConfigError("No value for '%s' defined in environment." % name)

