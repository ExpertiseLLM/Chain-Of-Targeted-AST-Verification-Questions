def get_logical_path_map(inventory, version):
	"""
	Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described.
	"""
	logical_path_in_state = {}
	logical_path_in_state[0] = set()
	logical_path_in_state[1] = set()
	logical_path_in_state[2] = set()
	logical_path_in_state[3] = set()
	logical_path_in_state[4] = set()
	for state in inventory.get_states():
		logical_path_in_state[state] = set()
		for log_path in inventory.get_logical_paths(state):
			logical_path_in_state[state].add(log_path)
	return logical_path_in_state