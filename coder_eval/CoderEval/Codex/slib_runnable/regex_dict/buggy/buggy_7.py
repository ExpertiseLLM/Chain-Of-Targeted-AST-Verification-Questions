def regex_dict(item):
	if not isinstance(item, dict):
		return item
	return dict(((re.compile(fnmatch.translate(k)), regex_dict(v)) for k, v in item.iteritems()))

