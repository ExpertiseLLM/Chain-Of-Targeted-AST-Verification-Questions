def split(s, platform='this'):
	"""
	Multi-platform variant of shlex.split() for command-line splitting.
For use with subprocess, for argv injection etc. Using fast REGEX.

platform: 'this' = auto from current platform;
          1 = POSIX;
          0 = Windows/CMD
          (other values reserved)
	"""
	if platform not in {'this', 'auto', 0, 1}:
		raise ValueError('platform must be one of this, auto, 0 or 1')
	return shlex.split(s, posix=platform == 0)

