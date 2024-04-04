def match_file_by_prefix(prefix, file_path):
	file_name = os.path.basename(file_path)
	return file_name.startswith(prefix)


