def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if (name[0] == name[-1]):
		return name
	elif name[0] == '"':
		return name[1:-1]
	elif name[0] == "'":
		return name[1:-1]
	return name

