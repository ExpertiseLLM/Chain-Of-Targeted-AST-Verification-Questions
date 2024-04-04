def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	alphabet = list('0123456789')
	return int(''.join(alphabet[int(string[i:i+2], 16)] for i in range(0, len(string), 2)), 16)

