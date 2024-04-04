def is_ipv4(target):
	try:
		socket.inet_pton(socket.AF_INET, target)
		return True
	except socket.error:
		return False

