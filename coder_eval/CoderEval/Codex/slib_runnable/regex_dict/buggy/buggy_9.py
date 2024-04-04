def regex_dict(item):
	regex_keys = {}
	for key, value in item.items():
		regex_keys[fnmatch_to_regex(key)] = value
	return regex_keys


