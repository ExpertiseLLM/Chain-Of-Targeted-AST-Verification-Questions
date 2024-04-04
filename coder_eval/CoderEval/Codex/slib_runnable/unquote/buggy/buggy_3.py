def unquote(name):
	if name[0] == '"':
		return name[1:-1].replace('""', '"')
	else:
		return name


