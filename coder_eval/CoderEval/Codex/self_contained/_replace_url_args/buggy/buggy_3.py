def _replace_url_args(url, url_args):
	for key, value in url_args.items():
		url = url.replace('<{}>'.format(key), value)
	return url

