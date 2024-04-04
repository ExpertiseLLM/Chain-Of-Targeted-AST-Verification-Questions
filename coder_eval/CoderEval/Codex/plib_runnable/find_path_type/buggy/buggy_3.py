def find_path_type(path):
	# TODO: check for valid version number
	n_path = os.path.join(path, "0=ocfl_object_1.0")
	if os.path.isdir(n_path):
		return "object"
	n_path = os.path.join(path, "0=ocfl_root_1.0")
	if os.path.isdir(n_path):
		return "root"
	if os.path.isfile(path):
		return "file"
	return "unknown"
