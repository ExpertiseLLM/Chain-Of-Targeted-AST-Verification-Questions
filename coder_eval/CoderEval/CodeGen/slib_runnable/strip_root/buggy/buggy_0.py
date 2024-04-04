def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	try:
		path = os.path.join(path, root)
		return path
	except OSError:
		raise

