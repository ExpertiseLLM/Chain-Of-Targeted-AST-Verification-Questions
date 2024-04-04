def files_list(path):
	"""
	Return the files in `path`
	"""
	files = []
	for _, dirs, files in os.walk(path):
		files.extend(dirs)
	return files

