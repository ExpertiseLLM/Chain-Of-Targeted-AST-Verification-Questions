def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	return host == 'localhost' or host == '127.0.0.1' or host == '::1' or host == '0.0.0.0' or host == '0.0.0.0/0' or host == '::1/0' or host == '::1/0/0'
	
