def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	try:
		path = path.split(root, 1)[1]
	except IndexError:
		raise ValueError('path must be without root')
	return path

