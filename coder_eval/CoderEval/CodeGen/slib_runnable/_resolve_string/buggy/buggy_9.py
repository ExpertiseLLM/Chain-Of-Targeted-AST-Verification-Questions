def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value.
If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if not isinstance(matcher, string_types):
		raise TypeError("matcher should be a string")
	if not os.path.exists(matcher):
		raise IOError("matcher does not exist")

	if os.path.isdir(matcher):
		matcher = os.path.abspath(matcher)

	if matcher in os.environ:
		return os.environ[matcher]

	if matcher.startswith('$'):
		matcher = matcher[1:]

	if matcher in os.environ:
		return os.environ[matcher]

	if matcher in sys.modules:
		return sys.modules[matcher]

	raise ValueError("matcher '{}' is not defined in environment".format(matcher))