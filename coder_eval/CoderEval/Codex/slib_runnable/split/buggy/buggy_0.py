def split(s, platform='this'):
	if platform == 'this':
		platform = (os.name == 'nt')
	assert platform in (0, 1), "Platform must be either 0 (Windows) or 1 (POSIX)"
	if platform:
		return shlex_split_posix(s)
	else:
		return shlex_split_ntcmd(s)

