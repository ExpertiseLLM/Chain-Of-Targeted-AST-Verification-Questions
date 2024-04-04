def find_path_type(path):
	files = glob('{}/0=*'.format(path))
	if len(files) == 0:
		return 'file'
	elif len(files) == 1:
		return 'object'
	elif len(files) == 2:
		return 'root'
	else:
		return 'unexpected'

