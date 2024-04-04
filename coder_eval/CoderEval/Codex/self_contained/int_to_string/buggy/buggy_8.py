def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		return alphabet[0]
	elif number < 0:
		raise ValueError("Only positive numbers can be converted to strings.")
	result = []
	while number > 0:
		result.append(alphabet[number % len(alphabet)])
		number //= len(alphabet)
	result.reverse()
	return "".join(result).rjust(padding, alphabet[0])


