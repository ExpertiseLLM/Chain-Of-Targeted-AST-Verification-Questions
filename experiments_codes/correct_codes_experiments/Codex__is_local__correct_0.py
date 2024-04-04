def is_local(host):
	return host in ['localhost', '127.0.0.1', '::1', 'localhost6', socket.gethostname()]


