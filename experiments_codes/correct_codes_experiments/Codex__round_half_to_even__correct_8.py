def round_half_to_even(n):
	if n % 1 <= 0.5:
		return int(n)
	elif n % 1 > 0.5:
		n = n + 1
		return int(n)


