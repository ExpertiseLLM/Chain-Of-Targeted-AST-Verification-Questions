def strip_root(path, root):
	if path.startswith(root):
		return path[len(root):]
	raise ValueError(path)


