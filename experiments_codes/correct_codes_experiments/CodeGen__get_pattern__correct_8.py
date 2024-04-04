def get_pattern(pattern, strip=True):
	"""
	This method converts the given string to regex pattern
	"""
	if strip:
		return re.compile(pattern.replace('\\', r'\\'))
	return re.compile(pattern)

