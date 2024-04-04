def size_to_bytes(size: str) -> int:
	size = size.upper()
	if size.endswith("K"):
		return int(size[:-1]) * 1000
	elif size.endswith("M"):
		return int(size[:-1]) * 1000 * 1000
	elif size.endswith("G"):
		return int(size[:-1]) * 1000 * 1000 * 1000
	elif size.endswith("T"):
		return int(size[:-1]) * 1000 * 1000 * 1000 * 1000
	else:
		return int(size)
