def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	if request.method == "POST" or request.method == "GET":
		return True
	else:
		return False