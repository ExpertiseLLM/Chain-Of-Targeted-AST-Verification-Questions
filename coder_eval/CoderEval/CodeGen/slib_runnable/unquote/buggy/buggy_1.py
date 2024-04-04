def unquote(name):
	"""
	Remove quote from the given name.
	"""
	if not isinstance(name, str):
		raise TypeError("name: expected a string, got %s" % type(name).__name__)
	if name == '':
		raise ValueError("name can't be an empty string: %r" % name)

	#