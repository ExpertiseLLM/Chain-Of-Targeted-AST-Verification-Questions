def find_path_type(path):
	path = os.path.abspath(path)
	if not os.path.exists(path):
		return 'Path does not exist'
	if not os.path.isdir(path):
		return 'Path is not a directory'
	if os.path.isfile(os.path.join(path, 'ocfl_object_1.0')):
		# Looks like an OCFL Object
		return 'object'
	namaste_files = glob.glob(os.path.join(path, '0=*'))
	if namaste_files:
		for namaste_file in namaste_files:
			if os.path.isfile(namaste_file):
				if os.path.basename(namaste_file) == '0=inventory.txt':
					return 'file'
				else:
					return 'Looks like an OCFL Object Version'
			if os.path.isdir(namaste_file):
				return '
