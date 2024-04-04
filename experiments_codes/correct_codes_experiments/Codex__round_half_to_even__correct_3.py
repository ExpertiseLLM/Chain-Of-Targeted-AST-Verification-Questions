def round_half_to_even(n):
	return round(n - 0.5) + (n % 1 > 0.5)


