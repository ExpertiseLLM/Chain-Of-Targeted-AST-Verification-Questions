def get_logical_path_map(inventory, version):
	if inventory.version_has_logical_path_map(version):
		return inventory.get_logical_path_map(version)
	else:
		return _get_logical_path_map(inventory, version)


