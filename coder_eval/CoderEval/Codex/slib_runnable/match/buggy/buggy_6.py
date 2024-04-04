def match(filename):
	return re.match(r'.*[.](wav|mp3|ogg|flac|wma)$', filename, re.IGNORECASE) is not None

