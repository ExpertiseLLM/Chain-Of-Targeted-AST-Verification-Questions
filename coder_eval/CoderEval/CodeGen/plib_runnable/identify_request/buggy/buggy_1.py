def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	return request.method == 'POST' and request.is_ajax()

