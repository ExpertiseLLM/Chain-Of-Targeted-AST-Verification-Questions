def is_fill_request_el(obj):
	"""
	Object contains executable methods 'fill' and'request'.
	"""
	return (obj.__class__.__name__ == 'fill' and
			hasattr(obj, 'fill'))

