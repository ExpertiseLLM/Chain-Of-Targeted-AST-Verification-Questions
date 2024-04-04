def round_half_to_even(n):
	return round(n) if n % 1 == 0.5 else round_half_up(n)

