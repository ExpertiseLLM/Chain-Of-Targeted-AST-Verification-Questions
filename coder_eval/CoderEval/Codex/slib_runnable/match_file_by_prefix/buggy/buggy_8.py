def match_file_by_prefix(prefix, file_path):
	return any(prefix in f for f in os.listdir(file_path))


