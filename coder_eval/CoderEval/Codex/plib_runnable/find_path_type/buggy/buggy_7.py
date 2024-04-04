def find_path_type(path):
	if not os.path.exists(path):
		return "path doesn't exist"
	if os.path.isdir(path):
		# Check for Storage Root
		for file in os.listdir(path):
			if file.startswith("0="):
				return "root"
		# Check for Object
		for file in os.listdir(path):
			if file.startswith("0="):
				return "object"
		return "directory"
	if os.path.isfile(path):
		return "file"
	return "unknown path type"


