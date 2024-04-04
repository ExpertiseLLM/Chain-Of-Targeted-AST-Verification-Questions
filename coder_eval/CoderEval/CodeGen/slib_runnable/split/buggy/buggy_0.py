def split(s, platform='this'):
	"""
	Multi-platform variant of shlex.split() for command-line splitting.
For use with subprocess, for argv injection etc. Using fast REGEX.

platform: 'this' = auto from current platform;
          1 = POSIX;
          0 = Windows/CMD
          (other values reserved)
	"""
	if platform == 'this':
		platform = os.getenv('PLATFORM') or 'this'
	elif platform == 'auto':
		platform = os.getenv('PLATFORM') or os.uname().machine
	if platform not in ('auto', 'this', '0', '1', '0.0', '1.0'):
		raise ValueError('invalid platform: %r' % platform)
	if platform == 'auto':
		platform = 'auto'
	return shlex.split(s, posix=platform == 'this')

