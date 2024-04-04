def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	if host == 'localhost':
		return True
	elif host.startswith('127.0.0.1'):
		return True
	else:
		return False

