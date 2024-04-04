def is_fill_request_el(obj):
	"""
	Object contains executable methods 'fill' and'request'.
	"""
	if isinstance(obj, dict):
		return ('fill',) in obj.keys()
	if isinstance(obj, list):
		return ('fill',) in obj[0].keys()
	if isinstance(obj, str):
		return obj in ('fill',)
	return False

