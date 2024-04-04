def size_to_bytes(size: str) -> int:
	if size == "":
		return 0

	suffixes = {
		"K": 1000,
		"M": 1000 * 1000,
		"G": 1000 * 1000 * 1000,
		"T": 1000 * 1000 * 1000 * 1000,
		"P": 1000 * 1000 * 1000 * 1000 * 1000,
	}

	multiplier = 1
	suffix = size[-1]
	if suffix in suffixes:
		multiplier = suffixes[suffix]
		size = size[:-1]
	return int(size) * multiplier


