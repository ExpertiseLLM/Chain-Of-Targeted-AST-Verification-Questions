def size_to_bytes(size: str) -> int:
	if not isinstance(size, str):
		raise TypeError("Unsupported type: '%s'" % type(size))

	size = size.upper()
	if not size.isdigit():
		if size[-1] not in ["K", "M", "G", "T"]:
			raise ValueError("Unknown size: '%s'" % size)
		if not size[:-1].isdigit():
			raise ValueError("Unknown size: '%s'" % size)

		factor = 1024
		if size[-1] == "K":
			exponent = 1
		elif size[-1] == "M":
			exponent = 2
		elif size[-1] == "G":
			exponent = 3
		elif size[-1] == "T":
			exponent = 4
		else:
			raise ValueError("Unknown size: '%s'" % size)

		return int(float(size[:-1]) * (factor ** exponent))
