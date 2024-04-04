def strip_root(path, root):
	if root == os.path.dirname(path):
		return os.path.basename(path)
	elif root == path:
		return ''

	if not path.startswith(root):
		raise Exception('path does not start with root')

	return path[len(root):].lstrip('/')


