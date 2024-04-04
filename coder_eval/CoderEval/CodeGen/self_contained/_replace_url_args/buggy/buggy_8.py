def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	if url_args is None:
		return url
	
	for key, value in url_args.items():
		if isinstance(value, string_types):
			url = url.replace(key, value)
	return url

