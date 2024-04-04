def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	try:
		addr = socket.gethostbyname(host)
		return addr == '127.0.0.1'
	except socket.error:
		return False

