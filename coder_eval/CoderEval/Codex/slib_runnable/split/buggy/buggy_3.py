def split(s, platform='this'):
	if platform=='this':
		platform=is_posix
	if platform:
		return _split_posix(s)
	else:
		return _split_windows(s)


