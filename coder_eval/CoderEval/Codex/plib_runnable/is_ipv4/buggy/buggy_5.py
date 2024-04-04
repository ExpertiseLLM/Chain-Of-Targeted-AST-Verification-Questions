def is_ipv4(target):
	try:
		socket.inet_aton(target)
		return True
	except socket.error:
		return False

