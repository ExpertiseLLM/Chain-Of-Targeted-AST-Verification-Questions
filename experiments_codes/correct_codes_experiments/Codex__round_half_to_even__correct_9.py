def round_half_to_even(n):
	if n % 2 == 0:
		return int(round(n))
	else:
		return int(round(n - 0.5))


