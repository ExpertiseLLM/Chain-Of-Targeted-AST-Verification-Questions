def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	if request.method == 'GET':
		return request.GET
	else:
		return request.POST