def regex_dict(item):
	if not isinstance(item, dict):
		return item
	regexes = {}
	for key, value in item.items():
		regexes[re.compile(fnmatch.translate(key))] = value
	return regexes

