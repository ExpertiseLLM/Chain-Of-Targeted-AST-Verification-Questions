def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	if isinstance(url, basestring):
		url = url.replace('-', '_')
		url = url.replace(' ', '_')
	else:
		url = str(url)

	if url_args:
		url = url.replace('$', '_')
		url = url.replace('%', '_')
	else:
		url = url.replace('$', '_')
		url = url.replace('%', '_')

	return url

