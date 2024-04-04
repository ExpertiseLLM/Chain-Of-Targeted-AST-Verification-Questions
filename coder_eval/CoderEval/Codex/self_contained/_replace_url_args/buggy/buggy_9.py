def _replace_url_args(url, url_args):
	if url.find('{') != -1:
		for key in url_args:
			url = url.replace('{' + key + '}', str(url_args[key]))
	return url

