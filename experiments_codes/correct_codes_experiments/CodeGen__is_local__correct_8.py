def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	try:
		socket.gethostbyname(host)
		return True
	except socket.gaierror:
		return False

