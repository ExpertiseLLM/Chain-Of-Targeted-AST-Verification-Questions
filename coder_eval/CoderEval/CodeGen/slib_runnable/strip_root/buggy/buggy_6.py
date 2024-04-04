def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	if root:
		if root[0] == '/':
			root = root[1:]
		if path[0] == '/':
			path = path[1:]
		if path and path[0] == '/':
			path = path[1:]
	elif path:
		if path[0] == '/':
			path = path[1:]
	if path == root:
		raise ValueError('cannot strip root')
	return path