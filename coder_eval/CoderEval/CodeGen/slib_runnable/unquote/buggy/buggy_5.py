def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if len(name) > 1:
		if name[:1] == '"' or name[:1] == "'":
			return name[1:-1].replace('\\' + name[:1] + '', '_')
	return name

