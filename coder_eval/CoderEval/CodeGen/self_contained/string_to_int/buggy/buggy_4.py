def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	number = 0
	for symbol in string:
		number += int(symbol) * (10 ** len(symbol))
	return number

