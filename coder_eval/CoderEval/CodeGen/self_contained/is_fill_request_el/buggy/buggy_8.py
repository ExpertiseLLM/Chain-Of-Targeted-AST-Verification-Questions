def is_fill_request_el(obj):
	"""
	Object contains executable methods 'fill' and'request'.
	"""
	return obj.__class__ is FillRequest or obj.__class__ is Request