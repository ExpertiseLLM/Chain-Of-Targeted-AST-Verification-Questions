def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	if number == 0:
		return alphabet[0]
	else:
		digits = []
		while number > 0:
			digits.append(alphabet[number % len(alphabet)])
			number //= len(alphabet)
		if padding is not None:
			while len(digits) < padding:
				digits.append(alphabet[0])
		digits.reverse()
		return ''.join(digits)


