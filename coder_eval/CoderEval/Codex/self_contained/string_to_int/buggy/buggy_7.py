def string_to_int(string: str, alphabet: List[str]) -> int:
	if not string:
		return 0

	return alphabet.index(string[0]) * (len(alphabet) ** (len(string) - 1)) + \
		string_to_int(string[1:], alphabet)
	
