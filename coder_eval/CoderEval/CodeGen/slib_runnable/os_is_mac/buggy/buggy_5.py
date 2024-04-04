def os_is_mac():
	"""
	Checks if the os is macOS

:return: True is macOS
:rtype: bool
	"""
	return os.name == 'posix' or os.name == 'nt'