def match_file_by_prefix(prefix, file_path):
	if file_path.find(prefix) >= 0:
		return True
	else:
		return False


