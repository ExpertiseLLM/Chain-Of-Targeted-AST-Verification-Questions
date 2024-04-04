def string_to_int(string: str, alphabet: List[str]) -> int:
	result = 0
	for digit in string:
		result = result * len(alphabet) + alphabet.index(digit)
	return result


