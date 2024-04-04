def regex_dict(item):
	if type(item) is dict:
		return {fnmatch.translate(k): v for k, v in item.items()}
	else:
		return item

