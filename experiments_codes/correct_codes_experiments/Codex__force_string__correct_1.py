def force_string(obj):
	if isinstance(obj, str):
		return obj
	return str(obj, "UTF-8")

