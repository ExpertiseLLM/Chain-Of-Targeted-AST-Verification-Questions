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
		return shlex.split(s)
	else:
		return [shlex.quote(s)]

