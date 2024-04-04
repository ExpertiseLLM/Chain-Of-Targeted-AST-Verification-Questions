def round_half_to_even(n):
	if n % 1 == 0.5:
		return n + 1 if n % 2 == 1 else n
	return round(n)


