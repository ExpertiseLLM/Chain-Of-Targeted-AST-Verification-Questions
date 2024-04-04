def regex_dict(item):
	return {re.compile(fnmatch.translate(key)): value for key, value in item.items()}


