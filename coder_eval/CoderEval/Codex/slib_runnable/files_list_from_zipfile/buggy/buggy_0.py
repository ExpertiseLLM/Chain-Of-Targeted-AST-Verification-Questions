def files_list_from_zipfile(zip_path):
	files = []
	with zipfile.ZipFile(zip_path) as zf:
		for info in zf.infolist():
			files.append(info.filename)
	return files


