def _resolve_string(matcher):
	try:
		value = _resolve_variable(matcher.group(1))
		if value is None:
			if matcher.group(2) is None:
				raise Error('No value defined for environment variable %s' % matcher.group(1))
			else:
				value = matcher.group(2)
	except Error as e:
		raise Error('Failed to resolve %s: %s' % (matcher.group(0), e))
	return value

