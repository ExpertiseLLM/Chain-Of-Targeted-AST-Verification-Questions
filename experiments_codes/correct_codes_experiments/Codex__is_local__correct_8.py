def is_local(host):
	if host == '127.0.0.1':
		return True
	if host == 'localhost':
		return True
	if host == '::1':
		return True
	if host == socket.gethostname():
		return True
	return False


