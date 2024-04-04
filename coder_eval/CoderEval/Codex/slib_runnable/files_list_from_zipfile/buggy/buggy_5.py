def files_list_from_zipfile(zip_path):
	if not zipfile.is_zipfile(zip_path):
		raise ValueError("Invalid zip file: %s" % (zip_path, ))

	zip_file = zipfile.ZipFile(zip_path)
	files = zip_file.namelist()
	zip_file.close()

	return files

