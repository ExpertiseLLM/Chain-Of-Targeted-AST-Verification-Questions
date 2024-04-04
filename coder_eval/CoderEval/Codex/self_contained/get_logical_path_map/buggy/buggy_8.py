def get_logical_path_map(inventory, version):
	logical_path_map = dict()
	for lp in inventory.logical_paths:
		if lp.version == version:
			if lp.logical_path not in logical_path_map:
				logical_path_map[lp.logical_path] = set()
			for cf in lp.content_files:
				logical_path_map[lp.logical_path].add(cf)
	return logical_path_map

