def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	for k, v in url_args.items():
		if k in url:
			url[k] = v
		else:
			url[k] = url.get(k, v)
	return url

