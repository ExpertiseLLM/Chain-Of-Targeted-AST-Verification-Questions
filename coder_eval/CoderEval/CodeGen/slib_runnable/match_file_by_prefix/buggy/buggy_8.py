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
	if os.path.splitext(file_path)[1] == '.html':
		return True
	elif os.path.splitext(file_path)[1] == '.pdf':
		return True
	elif os.path.splitext(file_path)[1] == '.mp3':
		return True
	elif os.path.splitext(file_path)[1] == '.png':
		return True
	else:
		return False

