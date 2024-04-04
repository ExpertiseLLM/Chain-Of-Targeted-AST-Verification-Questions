def find_path_type(path):
	path = Path(path)

	if not path.is_dir():
		return 'Not a directory'

	# Get the Namaste files
	namaste_paths = list(path.glob("0=*"))
	if not namaste_paths:
		return 'No Namaste files found'

	# Is it a Storage Root?
	if len(namaste_paths) == 1:
		if path.name.startswith("."):
			return 'root'
		else:
			return 'Object ID doesn\'t start with "."'

	# Is it an Object?
	if len(namaste_paths) == 2:
		for namaste_path in namaste_paths:
			# Check the file name
			if not namaste_path.name.startswith("0="):
				return 'Namaste file name doesn\'t start with "0="'

			# Check the file contents
			with open(namaste_path, 'r') as f
