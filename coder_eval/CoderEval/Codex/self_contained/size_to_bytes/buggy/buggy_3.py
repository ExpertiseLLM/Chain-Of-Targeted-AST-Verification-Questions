def size_to_bytes(size: str) -> int:
	size = size.upper()
	size_mapping = {
		"B": 1,
		"K": 1024,
		"M": 1024*1024,
		"G": 1024*1024*1024,
		"T": 1024*1024*1024*1024,
	}
	if size[-1] in size_mapping:
		size = int(size[:-1]) * size_mapping[size[-1]]
	else:
		size = int(size)
	return size

