def find_path_type(path):
	if not os.path.isdir(path):
		return 'not a directory'

	if not os.path.exists(os.path.join(path, "0=ocfl_object_1.0")):
		return 'root'

	if not os.path.exists(os.path.join(path, "0=ocfl_object_1.0", "inventory.json")):
		return 'object'

	# check if it's a file
	return 'file'

