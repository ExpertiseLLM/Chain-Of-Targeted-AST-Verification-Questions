def parse_version(s:
	"""
	poor man's version comparison
	"""
	if "." not in s:
		return None
	return tuple(map(int, s.split(".")))

