def get_pattern(pattern, strip=True):
	if strip:
		pattern = pattern.strip()
	if pattern.startswith('/') and pattern.endswith('/'):
		pattern = pattern[1:-1]
	return re.compile(pattern)
	
