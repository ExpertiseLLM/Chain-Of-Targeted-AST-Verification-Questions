def get_logical_path_map(inventory, version):
	logical_path_map = {}
	for content_file in inventory.get_all_content_files(version):
		for logical_path in content_file.logical_paths:
			if logical_path not in logical_path_map:
				logical_path_map[logical_path] = set()
			logical_path_map[logical_path].add(content_file)
	return logical_path_map

