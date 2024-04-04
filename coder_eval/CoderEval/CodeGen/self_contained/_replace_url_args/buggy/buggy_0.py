def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	if "?" in url:
		url = url.replace("?", "%s", 1)
	if "=" in url:
		url = url.replace("=", "%s", 1)
	url = url.replace("&", "%26", 1)
	url = url.replace("&&", "%26", 1)
	if "?" not in url:
		return url
	url = url.replace("%3A", ":", 1)
	url = url.replace("%3F", "?", 1)
	url = url.replace("%2B", "+", 1)
	url = url.replace("%2F", "/", 1)
	url = url.replace("%28", "(", 1)
	url = url.replace("%29", ")", 1)
	url = url.replace("%3F", "?", 1)
	url = url.replace("%3D", "=", 1)
	url = url.replace("%3F", "?", 1)
	url = url.replace("%3D", "=", 1)
	url = url.replace("%3A", ":", 1)
	url = url.replace("%3A", ":", 1)
	url = url.replace("%3A", ":", 1)
	url = url.replace("%3A", ":", 1)
	url = url.replace("%3A", ":", 1)
	return url

