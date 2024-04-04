def string_to_int(string: str, alphabet: List[str]) -> int:
	result = 0
	for i, c in enumerate(string):
		result += alphabet.index(c) * (len(alphabet) ** (len(string) - i - 1))
	return result

