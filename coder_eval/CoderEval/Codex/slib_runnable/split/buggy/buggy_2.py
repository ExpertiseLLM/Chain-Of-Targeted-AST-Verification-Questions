def split(s, platform='this'):
	if platform == 'this':
		platform = is_platform_posix
	if platform:
		if isinstance(s, unicode):
			return shlex.split(s.encode('utf-8'))
		else:
			return shlex.split(s)
	else:
		if not isinstance(s, unicode):
			s = s.decode('mbcs')
		return shlex_win.split(s)

