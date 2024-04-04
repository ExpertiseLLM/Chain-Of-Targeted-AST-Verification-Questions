def os_is_mac():
	"""
	Checks if the os is macOS

:return: True is macOS
:rtype: bool
	"""
	is_os_mac = False
	if platform.system() == 'Darwin':
		is_os_mac = (platform.system() == 'Darwin')
	elif platform.system() == 'Linux':
		is_os_mac = (platform.system() == 'Linux')
	elif platform.system() in ('Windows', 'Microsoft', 'Windows XP'):
		is_os_mac = (platform.system() == 'Windows')
	elif platform.system() in ('Linux', 'C#