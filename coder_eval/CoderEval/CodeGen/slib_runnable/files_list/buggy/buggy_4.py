def files_list(path):
	"""
	Return the files in `path`
	"""
	if not os.path.isdir(path):
		raise ValueError("`path` must be a directory")
	return os.listdir(path)