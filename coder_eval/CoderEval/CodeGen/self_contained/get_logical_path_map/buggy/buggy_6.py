def get_logical_path_map(inventory, version):
	"""
	Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described.
	"""
	paths = {}
	for path in inventory.logical_paths:
		if path in inventory.logical_paths[version]:
			paths[path] = set(inventory.logical_paths[version][path])
	return paths

