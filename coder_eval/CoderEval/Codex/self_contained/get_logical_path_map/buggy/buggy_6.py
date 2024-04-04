def get_logical_path_map(inventory, version):
	logical_path_map = collections.defaultdict(set)
	for path_in_state, content_files in inventory.path_map.items():
		if content_files:
			logical_path_map[path_in_state] = set(content_files)
		else:
			logical_path_map[path_in_state] = None
	for version in version.get_parent_versions():
		for path_in_state, content_files in version.inventory.path_map.items():
			if content_files:
				logical_path_map[path_in_state].update(content_files)
			else:
				logical_path_map[path_in_state] = None
	return dict(logical_path_map)

