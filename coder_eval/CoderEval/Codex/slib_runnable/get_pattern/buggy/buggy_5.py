def get_pattern(pattern, strip=True):
	if not pattern:
		return pattern
	if isinstance(pattern, str) and strip:
		pattern = pattern.strip()
	if isinstance(pattern, str):
		return re.compile(fnmatch.translate(pattern), re.IGNORECASE)
	return pattern

