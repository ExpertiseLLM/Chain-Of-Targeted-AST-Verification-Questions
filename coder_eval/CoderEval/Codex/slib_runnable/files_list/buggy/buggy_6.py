def files_list(path):
	return [f for f in listdir(path) if isfile(join(path, f))]

