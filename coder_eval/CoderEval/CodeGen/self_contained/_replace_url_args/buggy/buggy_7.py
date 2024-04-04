def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	if "?" in url:
		url = url.split("?")[0]
		if "," in url:
			url = re.sub(r"\w+", "%23", url)
			url_args = url_args.replace(r"%3D", url.replace(",", "%3D"))
			url_args = url_args.replace(r"%2F", "%2F")
		else:
			url_args = url_args.replace(r"%3D", "%3D")
			url_args = url_args.replace(r"%2F", "%2F")
			url_args = url_args.replace(r"%5B", "%5B")
			url_args = url_args.replace(r"%5D", "%5D")
		url_args = url_args.replace(r"%5B", "%5B")
		url_args = url_args.replace(r"%5D", "%5D")
	return url_args