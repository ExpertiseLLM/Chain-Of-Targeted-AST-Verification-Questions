def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if name[:1] == '"' or name[-1:] == '"':
		return name[1:-1].replace('\\'+name[:1]+'', '_')
	return name.replace('\\'+name[:1]+'', '_')