def _replace_url_args(url, url_args):
	if url_args is None:
		return url
	for arg in url_args:
		url = url.replace("$%s" % arg, url_args[arg])
	return url


