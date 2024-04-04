def get_pattern(pattern, strip=True):
	"""
	This method converts the given string to regex pattern
	"""
	if strip:
		pattern = pattern.strip()
	pattern = pattern.replace('\\','').replace('(', '\(').replace(')', '\)')
	pattern = pattern.replace('[', '\[').replace(']', '\]')
	return re.compile(pattern)

