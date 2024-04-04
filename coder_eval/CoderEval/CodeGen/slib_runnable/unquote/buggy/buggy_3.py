def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if not name:
		return ''
	elif name[0] == '"':
		end = name.index('"')
		name = name[1:end]
	elif name[0] == "'":
		end = name.index('"')
		name = name[1:end]
	return name