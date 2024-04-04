def get_logical_path_map(inventory, version):
	result = {}
	for item in inventory.findall('item'):
		version_specific_path = item.get('version_specific_path', None)
		if version_specific_path is None:
			logging.warn('Inventory item %s has no version_specific_path' % item)
			continue
		for version_info in item.findall('version_info'):
			if version_info.get('version') == version:
				logical_path = version_info.get('logical_path', None)
				if logical_path is None:
					logging.warn('Inventory item %s has no logical_path' % item)
					continue
				if logical_path in result:
					logging.warn('logical_path %s appears twice in inventory for version %s' % (logical_path, version))
				result[logical_path] = set(version_specific_path.split(';'))
	return
