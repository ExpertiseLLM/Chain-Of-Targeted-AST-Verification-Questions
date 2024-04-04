def unquote(name):
	if name[0] == name[-1] and name.startswith(("'", '"')):
		name = name[1:-1]
	return name


