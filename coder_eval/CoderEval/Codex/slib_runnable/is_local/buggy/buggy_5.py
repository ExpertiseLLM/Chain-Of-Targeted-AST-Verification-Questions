def is_local(host):
	if host == 'localhost':
		return True
	if host == '127.0.0.1':
		return True
	return False


