def force_string(obj):
	if isinstance(obj, bytes):
		return obj
	elif isinstance(obj, str):
		return obj.encode('utf-8')
	else:
		return str(obj).encode('utf-8')

