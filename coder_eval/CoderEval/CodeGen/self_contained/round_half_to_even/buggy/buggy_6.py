def round_half_to_even(n):
	"""
	>>> round_half_to_even(3)
    3
    >>> round_half_to_even(3.2)
    3
    >>> round_half_to_even(3.5)
    4
    >>> round_half_to_even(3.7)
    4
    >>> round_half_to_even(4)
    4
    >>> round_half_to_even(4.2)
    4
    >>> round_half_to_even(4.5)
    4
    >>> round_half_to_even(4.7)
    5

:param n:
:return:
	"""
	if n < 0:
		return 0
	elif n < 2:
		return 1
	else:
		return round(n/2)

