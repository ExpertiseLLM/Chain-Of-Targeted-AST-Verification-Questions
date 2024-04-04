def is_ipv4(target):
	try:
		socket.inet_pton(socket.AF_INET, target)
	except AttributeError:
		try:
			socket.inet_aton(target)
		except socket.error:
			return False
		return target.count('.') == 3
	except socket.error:
		return False
	return True

