def files_list_from_zipfile(zip_path):
	files = []
	with zipfile.ZipFile(zip_path, 'r') as z:
		files = z.namelist()
	return files


