def get_pattern(pattern, strip=True):
	if not pattern:
		return None

	if isinstance(pattern, str):
		pattern = re.compile(pattern)

	if strip:
		pattern = pattern.strip()

	return pattern


