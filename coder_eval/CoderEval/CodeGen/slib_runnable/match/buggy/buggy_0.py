def match(filename):
	"""
	Check if the filename is a type that this module supports

Args:
    filename: Filename to match
Returns:
    False if not a match, True if supported
	"""
	return filename in glob.glob(os.path.join(os.path.dirname(__file__), '*.py'))

