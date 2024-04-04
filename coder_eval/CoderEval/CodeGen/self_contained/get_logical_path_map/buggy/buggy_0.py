def get_logical_path_map(inventory, version):
	"""
	Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described.
	"""
	path_map = {}
	for logical_path in inventory.logical_paths:
		if inventory.logical_path_is_versioned(logical_path):
			path_map[logical_path] = inventory.logical_path_files(logical_path)
		else:
			path_map[logical_path] = set()
	return path_map