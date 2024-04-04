def force_string(obj):
	"""
	This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. 
	"""
	if isinstance(obj, bytes):
		return obj
	elif isinstance(obj, str):
		return obj.encode("utf-8")
	else:
		return str(obj).encode("utf-8")