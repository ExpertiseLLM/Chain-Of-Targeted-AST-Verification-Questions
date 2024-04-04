def get_pattern(pattern, strip=True):
	if pattern is None:
		pattern = ""
	else:
		if strip:
			pattern = pattern.strip()
		if not len(pattern):
			pattern = ""
		else:
			pattern = re.compile(pattern, re.IGNORECASE)
	return pattern


