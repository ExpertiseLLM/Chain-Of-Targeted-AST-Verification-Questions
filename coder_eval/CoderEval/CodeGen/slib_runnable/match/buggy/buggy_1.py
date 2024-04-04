def match(filename):
	"""
	Check if the filename is a type that this module supports

Args:
    filename: Filename to match
Returns:
    False if not a match, True if supported
	"""
	try:
		_match_type(filename)
		return True
	except:
		return False

