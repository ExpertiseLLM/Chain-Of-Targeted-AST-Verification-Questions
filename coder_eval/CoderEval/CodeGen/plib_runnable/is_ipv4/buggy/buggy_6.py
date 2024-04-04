def is_ipv4(target):
	"""
	Test if IPv4 address or not
    
	"""
	if isinstance(target, str) or isinstance(target, bytes):
		try:
			ipaddress.ip_address(target)
			return True
		except:
			return False
	else:
		return False

