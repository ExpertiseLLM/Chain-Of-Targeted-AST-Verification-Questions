def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.

The output has the most significant digit first.
	"""
	if number < 0:
		return '-' + int_to_string(-number)
	elif number < 10:
		return str(number)
	elif number > 10:
		return str(number)[-1] + int_to_string(number % 10)

