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
	if os.path.isdir(path):
		try:
			file_type = os.path.basename(path)
		except:
			file_type = 'unknown'
	else:
		file_type = 'unknown'
		
	if file_type == '0':
		return 'root'
	elif file_type == '0=*':
		return 'object'
	elif file_type == '*':
		return 'file'
	else:
		return 'other'

