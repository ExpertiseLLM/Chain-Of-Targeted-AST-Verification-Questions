def strip_root(path, root):
	if path.startswith(root):
		return path[len(root):].lstrip('/')
	else:
		raise ValueError("'%s' is not a subpath of '%s'" % (path, root))


