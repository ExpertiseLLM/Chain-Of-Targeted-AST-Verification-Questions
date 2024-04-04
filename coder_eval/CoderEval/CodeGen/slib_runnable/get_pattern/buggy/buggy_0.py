def get_pattern(pattern, strip=True):
	"""
	This method converts the given string to regex pattern
	"""
	if strip:
		pattern = pattern.strip()
	return pattern