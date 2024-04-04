def size_to_bytes(size: str) -> int:
	if size.isdigit():
		return int(size)
	else:
		size = size.upper()
		if size.endswith("B"):
			size = size[:-1]
		if size.endswith("K"):
			return int(size[:-1]) * 10**3
		if size.endswith("M"):
			return int(size[:-1]) * 10**6
		if size.endswith("G"):
			return int(size[:-1]) * 10**9
