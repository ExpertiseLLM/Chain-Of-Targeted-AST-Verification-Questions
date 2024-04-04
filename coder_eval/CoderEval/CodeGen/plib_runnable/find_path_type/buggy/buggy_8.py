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
	if path == '':
		return 'root'
	if path[0] == '0':
		return 'object'
	if path[0] == '*':
		return 'file'
	return path
