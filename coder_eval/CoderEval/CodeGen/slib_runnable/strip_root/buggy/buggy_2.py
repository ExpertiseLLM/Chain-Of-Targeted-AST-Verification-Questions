def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	if not path or not root:
		raise ValueError("path or root must be a string")
	if not path.startswith(root):
		raise ValueError("path must start with root")
	return path[len(root):]

