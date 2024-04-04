def force_string(obj):
	if is_string(obj):
		return obj.encode()
	return obj

