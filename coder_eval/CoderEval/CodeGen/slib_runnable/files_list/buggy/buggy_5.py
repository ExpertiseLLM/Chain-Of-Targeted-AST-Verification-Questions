def files_list(path):
	"""
	Return the files in `path`
	"""
	files = []
	for root, dirs, files in os.walk(path):
		for file in files:
			files.append(os.path.join(root, file))
	return files

