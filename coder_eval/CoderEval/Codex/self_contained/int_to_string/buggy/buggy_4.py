def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
	# The number will be written as s[i] + s[i-1] ... + s[0] * base^i
	# For example, base=10, number=12345: s = [5, 4, 3, 2, 1]
	# Because 5 + 4*10 + 3*100 + 2*1000 + 1*10000 = 12345
	s = []
	while number > 0:
		number, digit = divmod(number, len(alphabet))
		s.append(alphabet[digit])
	s.reverse()
	# Add padding, if needed
	if padding is not None:
		s.extend(alphabet[0] * (padding - len(s)))
	return ''.join(s)


