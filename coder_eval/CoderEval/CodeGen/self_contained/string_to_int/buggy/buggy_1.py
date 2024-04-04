def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	num = 0
	for char in string:
		num = num * 26 + ord(char) - ord('A')
	return num

