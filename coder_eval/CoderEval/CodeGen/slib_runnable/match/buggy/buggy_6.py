def match(filename):
	"""
	Check if the filename is a type that this module supports

Args:
    filename: Filename to match
Returns:
    False if not a match, True if supported
	"""
	return filename.lower().endswith(".dll") or filename.lower().endswith(".so") or filename.lower().endswith(".pyd")

