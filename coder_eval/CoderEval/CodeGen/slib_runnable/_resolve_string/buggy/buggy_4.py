def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	env_name = matcher.group(1)
	if env_name not in os.environ:
		raise ValueError(f"{env_name} is not defined in environment")
	return os.environ[env_name]