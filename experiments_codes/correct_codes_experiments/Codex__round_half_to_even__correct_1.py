def round_half_to_even(n):
	if n % 1 > 0.5:
		return int(n) + 1
	elif n % 1 < 0.5:
		return int(n)
	else:
		if int(n) % 2 == 0:
			return int(n)
		else:
			return int(n) + 1


