def regex_dict(item):
	regex_keys = {}
	for key, value in item.items():
		regex_keys[fnmatch.translate(key)] = value
	return regex_keys

