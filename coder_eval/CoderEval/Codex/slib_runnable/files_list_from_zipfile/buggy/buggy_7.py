def files_list_from_zipfile(zip_path):
	with zipfile.ZipFile(zip_path) as zip_file:
		return zip_file.namelist()


