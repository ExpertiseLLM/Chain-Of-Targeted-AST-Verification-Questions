def files_list(path):
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			yield file


