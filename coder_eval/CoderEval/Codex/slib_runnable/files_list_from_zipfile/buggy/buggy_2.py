def files_list_from_zipfile(zip_path):
	zip_path = os.path.abspath(zip_path)
	zip_file = zipfile.ZipFile(zip_path)
	return zip_file.namelist()

