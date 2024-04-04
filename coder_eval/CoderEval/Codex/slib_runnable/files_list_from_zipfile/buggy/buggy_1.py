def files_list_from_zipfile(zip_path):
	files = []
	with zipfile.ZipFile(zip_path) as zip_file:
		for file in zip_file.namelist():
			files.append(file)
	return files


