def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	if os.getenv('HOST') is None:
		return False
	return os.getenv('HOST') == host