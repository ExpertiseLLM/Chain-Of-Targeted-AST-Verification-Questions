def string_to_int(string: str, alphabet: List[str]) -> int:
	value = 0
	for c in string:
		value = alphabet.index(c) + value * len(alphabet)
	return value

