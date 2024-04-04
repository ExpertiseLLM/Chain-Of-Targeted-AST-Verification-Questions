def find_path_type(path):
	"""
	Return a string indicating the type of thing at the given path.

Return values:
    'root' - looks like an OCFL Storage Root
    'object' - looks like an OCFL Object
    'file' - a file, might be an inventory
    other string explains error description

Looks only at "0=*" Namaste files to determine the directory type.
	"""
	if path == '0':
		return 'root'
	elif path == '1':
		return 'object'
	elif path == '2':
		return 'file'
	else:
		raise ValueError("path must be either '0' or '1'")

