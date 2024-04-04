def parse_version(s:
	"""
	poor man's version comparison
	"""
	version_parts = s.split(".")

	if len(version_parts) == 1:
		return 1
	else:
		return int(version_parts[0])

	return int(s.split(".")[0])