def get_logical_path_map(inventory, version):
	result = {}
	for item in inventory.findall('content'):
		file = item.attrib['file']
		if 'version' in item.attrib:
			if item.attrib['version'] != version:
				continue
		logical_path_in_state = item.attrib['path'].strip('/')
		if logical_path_in_state not in result:
			result[logical_path_in_state] = set()
		result[logical_path_in_state].add(file)
	return result

