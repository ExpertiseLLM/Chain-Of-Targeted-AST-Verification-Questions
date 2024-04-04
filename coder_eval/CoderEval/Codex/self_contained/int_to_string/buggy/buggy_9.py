def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	base = len(alphabet)
	digits = []
	if number == 0:
		digits.append(alphabet[0])
	while number > 0:
		digits.append(alphabet[number % base])
		number //= base
	if padding is not None:
		digits.extend(alphabet[0] * (padding - len(digits)))
	return "".join(reversed(digits))


