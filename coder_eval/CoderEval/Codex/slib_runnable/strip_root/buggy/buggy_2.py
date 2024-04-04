def strip_root(path, root):
	if not path.startswith(root):
		raise Exception('%s is not a subpath of %s' % (path, root))
	return path[len(root):]


