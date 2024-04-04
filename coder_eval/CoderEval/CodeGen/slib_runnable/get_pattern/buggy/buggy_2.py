def get_pattern(pattern, strip=True):
	"""
	This method converts the given string to regex pattern
	"""
	global pattern_regex
	pattern_regex = pattern
	if strip:
		pattern = pattern.strip()
	return pattern

