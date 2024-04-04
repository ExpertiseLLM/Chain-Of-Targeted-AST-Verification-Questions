def round_half_to_even(n):
	if n % 1 < 0.5 or n % 1 > 0.5:
		return int(n)
	elif n % 1 == 0.5:
		if n % 2 == 0:
			return int(n)
		else:
			return int(n) + 1


