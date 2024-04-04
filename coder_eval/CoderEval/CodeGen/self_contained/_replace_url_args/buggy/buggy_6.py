def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	if url.endswith('.json'):
		return url
	elif url.endswith('.xlsx'):
		return url

	#