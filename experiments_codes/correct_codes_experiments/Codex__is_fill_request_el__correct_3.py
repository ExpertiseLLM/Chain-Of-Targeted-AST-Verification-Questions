def is_fill_request_el(obj):
	return hasattr(obj, 'fill') and hasattr(obj, 'request') and callable(obj.fill) and callable(obj.request)

