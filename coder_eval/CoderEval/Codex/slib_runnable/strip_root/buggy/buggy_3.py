def strip_root(path, root):
	if not path.startswith(root):
		raise ValueError("%s does not start with %s" % (path, root))
	return path[len(root):]


