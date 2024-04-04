def parse_version(s:
	"""
	poor man's version comparison
	"""
	if s.find('.') >= 0:
		v = s.split('.')
		v = list(map(int, v))
		return v
	else:
		return [int(s)]

