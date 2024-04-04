def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if len(name) > 1:
		result = name[1:].replace('%', '')
		if result[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			result = '%' + result
	return result

