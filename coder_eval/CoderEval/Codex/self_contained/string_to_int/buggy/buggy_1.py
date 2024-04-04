def string_to_int(string: str, alphabet: List[str]) -> int:
	result = 0
	for letter in string:
		result *= len(alphabet)
		result += alphabet.index(letter)
	return result

