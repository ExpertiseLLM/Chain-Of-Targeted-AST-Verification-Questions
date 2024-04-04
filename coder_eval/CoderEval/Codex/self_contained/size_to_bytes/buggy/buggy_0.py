def size_to_bytes(size: str) -> int:
	size = size.upper()
	if re.match(r'^-?\d+$', size):
		return int(size)
	elif re.match(r'^-?\d+[KMGTPEZY]?$', size):
		matches = re.match(r'^-?(\d+)([KMGTPEZY])?$', size)
		num, prefix = int(matches.group(1)), matches.group(2)
		if num < 0:
			return -size_to_bytes(str(-num) + prefix)
		elif prefix == 'K':
			return num * 1000
		elif prefix == 'M':
			return num * 1000 * 1000
		elif prefix == 'G':
			return num * 1000 * 1000 * 1000
		elif prefix == 'T':
			return num * 1000 * 1000 * 1000 * 1000
		elif prefix == 'P':
			return num * 1000 * 1000 * 1000 * 1000 * 1000
		
