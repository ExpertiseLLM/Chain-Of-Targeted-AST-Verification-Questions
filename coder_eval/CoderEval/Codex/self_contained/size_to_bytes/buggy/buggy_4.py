def size_to_bytes(size: str) -> int:
	if not isinstance(size, str):
		raise TypeError("size_to_bytes: size must be a string")
	if size.isdigit():
		return int(size)
	else:
		size_regexp = re.compile(r"([0-9]+)\s*(?:([kmgtpezy]?i?b))?$", re.IGNORECASE)
		size_match = size_regexp.match(size)
		if size_match:
			size = float(size_match.group(1))
			if size_match.group(2):
				unit = size_match.group(2).lower()
				if unit == "b":
					return int(size)
				else:
					units = ["k", "m", "g", "t", "p", "e", "z", "y"]
					exponent = units.index(unit[0]) + 1
					if unit
