def find_path_type(path):
	if not os.path.isdir(path):
		return 'not_dir'
	if os.path.islink(path):
		return 'link'
	if os.path.exists(os.path.join(path, 'OCFL_ROOT_INFO.txt')):
		return 'root'
	if os.path.exists(os.path.join(path, 'inventory.json')):
		return 'object'
	if os.path.exists(os.path.join(path, '0=ocfl_object_1.0')):
		return 'object'
	if os.path.exists(os.path.join(path, 'inventory.xml')):
		return 'object'
	if os.path.exists(os.path.join(path, '0=ocfl_object_1.0')):
		return 'object'
	if os.path.exists(os.path.join(path, '0=content')):
		return 'object'
	if os.path.exists(os
