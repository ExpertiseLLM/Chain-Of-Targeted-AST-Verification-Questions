def match_file_by_prefix(prefix, file_path):
	prefix = prefix.lower()
	file_path = file_path.lower()
	return file_path.startswith(prefix) and file_path != prefix


