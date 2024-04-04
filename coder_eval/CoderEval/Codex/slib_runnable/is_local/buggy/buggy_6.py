def is_local(host):
	try:
		return socket.gethostbyname(host) == '127.0.0.1'
	except Exception:
		return False


