def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	return_value = ""
	while number != 0:
		digit = number % len(alphabet)
		number = number // len(alphabet)
		return_value = alphabet[digit] + return_value
	if padding is not None:
		return_value = return_value.rjust(padding, alphabet[0])
	return return_value


