def get_pattern(pattern, strip=True):
	if strip:
		pattern = pattern.strip()
	if not pattern:
		return None
	return re.compile(pattern, re.I)

