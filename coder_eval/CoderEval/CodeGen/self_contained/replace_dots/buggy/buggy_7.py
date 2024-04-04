def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
	"""
	return re.sub(r'\.', arg, value)

