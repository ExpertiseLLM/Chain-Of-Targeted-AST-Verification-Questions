def get_logical_path_map(inventory, version):
	logical_path_map = collections.defaultdict(set)
	for logical_path, file_identifier in inventory.get_files(version).iteritems():
		physical_path = inventory.get_file_physical_path(file_identifier)
		logical_path_map[logical_path].add(physical_path)
	return logical_path_map

