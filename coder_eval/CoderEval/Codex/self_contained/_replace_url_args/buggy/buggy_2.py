def _replace_url_args(url, url_args):
	_url = url
	for key, value in url_args.iteritems():
		_url = _url.replace("<%s>" % key, value)
	return _url


