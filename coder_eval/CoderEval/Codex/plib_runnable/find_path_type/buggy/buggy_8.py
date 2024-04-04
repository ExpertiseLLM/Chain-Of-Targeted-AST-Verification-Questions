def find_path_type(path):
	path = os.path.abspath(path)
	if not os.path.isdir(path):
		return "Path is not a directory"
	if not os.path.exists(os.path.join(path, "0=ocfl_object_1.0")):
		return "Path is not a directory"
	if not os.path.exists(os.path.join(path, "0=ocfl_object_1.0", "inventory.json")):
		return "Path is not an OCFL Object"
	return "object"


