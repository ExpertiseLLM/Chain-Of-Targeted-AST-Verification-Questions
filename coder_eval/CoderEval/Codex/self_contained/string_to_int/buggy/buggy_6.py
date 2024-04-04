def string_to_int(string: str, alphabet: List[str]) -> int:
	if len(string) == 0:
		return 0
	else:
		return alphabet.index(string[0]) + len(alphabet) * string_to_int(string[1:], alphabet)

