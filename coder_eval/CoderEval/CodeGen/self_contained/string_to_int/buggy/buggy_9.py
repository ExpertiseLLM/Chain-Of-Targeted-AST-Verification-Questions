def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	return int("".join(map(str, string)), base=10)