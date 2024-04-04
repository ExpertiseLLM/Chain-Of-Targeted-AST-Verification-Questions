def int_to_string(number:
	"""
	Convert a number to a string, using the given alphabet.

The output has the most significant digit first.
	"""
	assert 0 <= number <= 9999
	assert len(alphabet) == len(alphabet.upper())
	assert not any(number == n for n in range(1, 10))

	#