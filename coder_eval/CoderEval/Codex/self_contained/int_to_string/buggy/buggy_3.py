def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	# Example:
	# int_to_string(123, ['a', 'b', 'c', 'd'])
	# => 'dcd'

	if padding is not None:
		number += len(alphabet) ** padding
		padding = None

	base = len(alphabet)
	output = ''
	while number > 0:
		output += alphabet[number % base]
		number //= base

	if padding is not None:
		output += alphabet[0] * padding

	return output[::-1]

