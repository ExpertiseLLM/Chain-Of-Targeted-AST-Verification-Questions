def size_to_bytes(size: str) -> int:
	size = size.upper()
	if not re.search(r'^\d+[KMGT]?$', size):
		raise ValueError("Invalid file size: %s" % size)

	# Remove the non-digit characters from the string.
	size = re.sub("\D", "", size)

	multiplier = 1
	if size[-1] == 'K':
		multiplier = 1000
		size = size[:-1]
	elif size[-1] == 'M':
		multiplier = 1000 * 1000
		size = size[:-1]
	elif size[-1] == 'G':
		multiplier = 1000 * 1000 * 1000
		size = size[:-1]
	elif size[-1] == 'T':
		multiplier = 1000 * 1000 * 1000 * 1000
		size = size[:-1]

	size = int(size)
	size *= multiplier

	return size


