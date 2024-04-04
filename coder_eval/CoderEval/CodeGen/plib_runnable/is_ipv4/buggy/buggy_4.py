def is_ipv4(target):
	"""
	Test if IPv4 address or not
    
	"""
	if not isinstance(target, str) or not target:
		return False
	if re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', target):
		return True
	return False

