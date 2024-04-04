def string_to_int(string: str, alphabet: List[str]) -> int:
	val = 0
	power = 1
	for digit in reversed(string):
		val += power * alphabet.index(digit)
		power *= len(alphabet)
	return val

