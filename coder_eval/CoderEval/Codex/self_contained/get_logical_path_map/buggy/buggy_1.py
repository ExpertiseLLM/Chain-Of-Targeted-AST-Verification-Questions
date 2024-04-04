def get_logical_path_map(inventory, version):
	path_to_files = {}
	for (logical_path, content_file) in inventory.get_version_content_files(version):
		path_to_files.setdefault(logical_path, set()).add(content_file)
	return path_to_files


