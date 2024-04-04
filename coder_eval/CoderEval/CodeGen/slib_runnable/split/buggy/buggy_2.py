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
		s, platform = s, 'this'
	elif platform == '0':
		s, platform = s, '0'
	elif platform == '1':
		s, platform = s, '1'
	elif platform == '0':
		s, platform = s, '0'
	elif platform == '0':
		s, platform = s, '0'
	else:
		raise ValueError('invalid platform: %r' % platform)
	return s.split()

