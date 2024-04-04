def get_pattern(pattern, strip=True):
	if pattern is None:
		return None
	pattern = pattern.strip()
	if strip:
		return re.compile(pattern)
	return re.compile(pattern, re.DOTALL)

