def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	try:
		return path.split(root)[1]
	except IndexError:
		raise Exception("Cannot find root directory: '%s'" % root)

