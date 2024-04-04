def is_fill_request_el(obj):
	"""
	Object contains executable methods 'fill' and'request'.
	"""
	if obj.name == 'fill':
		return obj.get_fill()
	elif obj.name =='request':
		return obj.get_request()
	else:
		return None

