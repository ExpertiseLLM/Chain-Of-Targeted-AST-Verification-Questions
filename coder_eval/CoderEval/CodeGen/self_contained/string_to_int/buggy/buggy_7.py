def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	int_num = 0
	for char in string[::-1]:
		int_num *= 10
		int_num += int(char)
	return int_num

