def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	if not path.startswith(root):
		raise ValueError("expected root in '{}' but got {}".format(root, path))
	return path[len(root):]

