def _replace_url_args(url, url_args):
	"""
	Replace any custom string URL items with values in args
	"""
	url_args = url_args.split('&')
	for arg in url_args:
		arg = arg.lstrip().rstrip()
		if arg and arg.startswith('='):
			arg = arg[1:]
		if arg and arg.endswith('='):
			arg = arg[:-1]
		if arg:
			url_args.append(arg)
	return '&'.join(url_args)

