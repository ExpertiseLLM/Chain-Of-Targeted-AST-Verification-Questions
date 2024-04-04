def get_logical_path_map(inventory, version):
	logical_path_map = collections.defaultdict(set)
	for content_file in inventory.content_files:
		if content_file.version == version:
			logical_path_map[content_file.logical_path_in_state].add(content_file)
	return logical_path_map

