def string_to_int(string:
	"""
	Convert a string to a number, using the given alphabet.

The input is assumed to have the most significant digit first.
	"""
	nums = []
	for c in string:
		if c.isalpha():
			nums.append(int(c))
		else:
			nums.append(ord(c) - ord('A') + 10)
	return nums#