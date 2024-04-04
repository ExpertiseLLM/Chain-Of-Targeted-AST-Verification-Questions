def is_local(host):
	if host == 'localhost' or host == '127.0.0.1' or host == '::1':
		return True
	return False


