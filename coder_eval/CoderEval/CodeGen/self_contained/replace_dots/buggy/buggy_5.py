def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
	"""
	if isinstance(value, str):
		if value == ".":
			value = arg
	return value

