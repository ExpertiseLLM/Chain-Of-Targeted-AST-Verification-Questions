def regex_dict(item):
	# this is a bit of a hack, but it works
	new_dict = {}
	for key in item:
		new_key = fnmatch.translate(key)
		new_dict[new_key] = item[key]
	return new_dict


