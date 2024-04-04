def force_string(obj):
	"""
	This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. 
	"""
	if isinstance(obj, str) or isinstance(obj, unicode):
		return obj
	if isinstance(obj, bytes):
		return obj.decode('utf-8')
	raise TypeError("Unable to force string")