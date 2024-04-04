def split(s, platform='this'):
	if platform is None or platform == 'this':
		platform = (os.name == 'nt')
	elif isinstance(platform, bool):
		platform = not platform
	elif isinstance(platform, int):
		platform = bool(platform)
	else:
		raise ValueError("unsupported platform")

	if platform:
		# POSIX-like - shlex.split()
		return shlex.split(s)
	else:
		# Windows-like - CMD style
		return cmd_split(s)
