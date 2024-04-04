def match_file_by_prefix(prefix, file_path):
	"""
	Identify if a `file_path` belongs to a document package by a given `prefix`

Retorna `True` para documentos pertencentes a um pacote.

Parameters
----------
prefix : str
    Filename prefix
file_path : str
    File path
Returns
-------
bool
    True - file belongs to the package
	"""
	if os.path.isfile(file_path):
		filenames = os.listdir(file_path)
		for filename in filenames:
			if filename.startswith(prefix):
				return True
	return False

