def force_string(obj):
	"""
	This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. 
	"""
	if isinstance(obj, six.binary_type):
		return obj
	elif isinstance(obj, six.text_type):
		return obj.encode('utf-8')
	else:
		raise TypeError('force_string() argument must be of type str or unicode.')

