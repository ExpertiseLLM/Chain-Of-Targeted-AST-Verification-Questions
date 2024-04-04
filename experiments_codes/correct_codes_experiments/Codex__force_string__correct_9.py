def force_string(obj):
	if isinstance(obj, bytes):
		return obj.decode('UTF-8')
	return obj

