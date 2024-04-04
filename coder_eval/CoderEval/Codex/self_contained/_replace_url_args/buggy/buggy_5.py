def _replace_url_args(url, url_args):
	for arg in url_args:
		url = url.replace("<{0}>".format(arg), str(url_args[arg]))
	return url


