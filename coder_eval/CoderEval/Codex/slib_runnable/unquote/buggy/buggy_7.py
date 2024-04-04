def unquote(name):
	if name and name[0] in '\'"':
		name = name[1:-1]
	return name

