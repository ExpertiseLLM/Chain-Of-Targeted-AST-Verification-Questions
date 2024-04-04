def _resolve_string(matcher):
	variable_name = matcher.group(1)
	if variable_name not in os.environ:
		if matcher.group(2):
			return matcher.group(2)
		else:
			raise Error(f'Variable {variable_name} not defined in environment')
	return os.environ[variable_name]


