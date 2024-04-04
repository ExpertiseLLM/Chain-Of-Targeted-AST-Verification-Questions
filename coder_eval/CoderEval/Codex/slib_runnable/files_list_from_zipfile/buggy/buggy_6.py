def files_list_from_zipfile(zip_path):
	with ZipFile(zip_path, 'r') as zip_file:
		return zip_file.namelist()


