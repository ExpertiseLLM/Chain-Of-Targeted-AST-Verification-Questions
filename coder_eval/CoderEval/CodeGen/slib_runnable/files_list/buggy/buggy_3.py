def files_list(path):
	"""
	Return the files in `path`
	"""
	files = []
	for f in sorted(os.listdir(path)):
		if os.path.isfile(os.path.join(path, f)):
			files.append(f)
		else:
			for sub_path in files_list(os.path.join(path, f)):
				files.append(sub_path)
	return files