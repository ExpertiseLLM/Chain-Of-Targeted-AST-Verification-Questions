def string_to_int(string: str, alphabet: List[str]) -> int:
	val = 0
	for c in string:
		val *= len(alphabet)
		val += alphabet.index(c)
	return val


