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
	if not os.path.exists(file_path):
		return False
	if not os.path.isfile(file_path):
		return False
	for line in open(file_path, "r"):
		if line.startswith(prefix):
			return True
	return False

