def regex_dict(item):
	result = {}
	for key in item:
		result[fnmatch.translate(key)] = item[key]
	return result


