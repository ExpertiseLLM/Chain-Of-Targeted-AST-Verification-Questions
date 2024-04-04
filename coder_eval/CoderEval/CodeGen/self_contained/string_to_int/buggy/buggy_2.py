def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	int_string = 0
	for char in string:
		int_string += (ord(char) - ord('0')) * (26**(len(string)-1))
	return int_string

