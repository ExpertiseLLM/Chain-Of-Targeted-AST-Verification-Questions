def unquote(name):
	if name.startswith('"') and name.endswith('"'):
		name = name[1:-1]
	return name


