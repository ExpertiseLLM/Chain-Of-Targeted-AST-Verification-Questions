def round_half_to_even(n):
	n_int = int(n)
	diff = n - n_int
	if diff == 0.5:
		if n_int % 2 == 0:
			return n_int
		else:
			return n_int + 1
	elif diff > 0.5:
		return n_int + 1
	else:
		return n_int

