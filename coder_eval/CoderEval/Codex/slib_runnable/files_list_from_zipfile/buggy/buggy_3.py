def files_list_from_zipfile(zip_path):
	with zipfile.ZipFile(zip_path, mode='r') as f:
		return f.namelist()


