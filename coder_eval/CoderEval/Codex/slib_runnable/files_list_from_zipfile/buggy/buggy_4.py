def files_list_from_zipfile(zip_path):
	files = []
	with zipfile.ZipFile(zip_path) as zf:
		for info in zf.infolist():
			if info.filename.startswith('__MACOSX'):
				continue
			files.append(info.filename)
	return files


