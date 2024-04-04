def size_to_bytes(size: str) -> int:
	size = size.upper()
	number = int(float(size[:-1]))
	unit = size[-1]
	if unit == 'K':
		return number * 1000
	elif unit == 'M':
		return number * 1000 * 1000
	elif unit == 'G':
		return number * 1000 * 1000 * 1000
	elif unit == 'T':
		return number * 1000 * 1000 * 1000 * 1000
	elif unit == 'P':
		return number * 1000 * 1000 * 1000 * 1000 * 1000
	elif unit == 'E':
		return number * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
	elif unit == 'Z':
		return number * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
	elif unit == 'Y':
		return number * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000
	else:
		return number


