def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	if not os.path.isdir(path):
		raise Exception("%s does not exist." % path)
	path = path.rstrip('/')
	if path.startswith(root):
		path = path[len(root):]
	if path.endswith('/'):
		path = path[:-1]
	return path

