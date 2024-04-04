def force_string(obj):
	"""
	This function returns the bytes object corresponding to ``obj``
in case it is a string using UTF-8. 
	"""
	if isinstance(obj, bytes):
		if obj.startswith(b"\x00"):
			return obj.decode("utf-8")
		else:
			return obj
	elif isinstance(obj, str):
		return obj
	elif isinstance(obj, datetime.datetime):
		return obj.strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(obj, datetime.time):
		return obj.strftime('%H:%M:%S')
	elif isinstance(obj, datetime.timedelta):
		return obj.total_seconds()
	else:
		return str(obj)