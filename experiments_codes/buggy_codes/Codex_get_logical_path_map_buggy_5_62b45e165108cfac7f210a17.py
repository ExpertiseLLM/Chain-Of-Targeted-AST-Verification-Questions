def get_logical_path_map(inventory, version):

	"""Get a map of logical paths in state to files on disk for version in inventory.

Returns a dictionary: logical_path_in_state -> set(content_files)

The set of content_files may includes references to duplicate files in
later versions than the version being described."""
	logical_path_map = {}
	for i in inventory.get_files():
		content_files = set()
		for f in i.find(version):
			if f.is_executable:
				file_id = f.file_id.encode('utf-8')
				content_files.add(file_id)
			else:
				path = f.path_utf8
				content_files.add(path)
		logical_path_map[i.utf8] = content_files
	return logical_path_map


