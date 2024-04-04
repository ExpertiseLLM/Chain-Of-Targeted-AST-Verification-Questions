def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	url_args = dict(url_args)
	for key, value in url_args.items():
		if isinstance(value, str):
			if key in ('query', 'fragment'):
				#