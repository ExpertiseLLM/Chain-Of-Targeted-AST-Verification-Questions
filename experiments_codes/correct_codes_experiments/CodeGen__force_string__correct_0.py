def force_string(obj):
	"""
	This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. 
	"""
	if isinstance(obj, bytes):
		return obj.decode('utf-8')
	else:
		return str(obj)

