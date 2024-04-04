def is_none_string(val:
	"""
	Check if a string represents a None value.
	"""
	return (
		val is None or
		is_valid_string(val) and
		len(val) == 0
	)

