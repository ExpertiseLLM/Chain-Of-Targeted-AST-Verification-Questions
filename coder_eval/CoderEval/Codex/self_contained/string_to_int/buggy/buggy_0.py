def string_to_int(string: str, alphabet: List[str]) -> int:
	return sum(
		alphabet.index(char) * len(alphabet) ** exponent
		for exponent, char in enumerate(string[::-1])
	)


