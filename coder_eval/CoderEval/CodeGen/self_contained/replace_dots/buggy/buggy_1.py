def replace_dots(value, arg):
	"""
	Replaces all values of '.' to arg from the given string
	"""
	for i in range(len(value)):
		if value[i] == '.':
			value = value.replace('.', arg)
	return value

