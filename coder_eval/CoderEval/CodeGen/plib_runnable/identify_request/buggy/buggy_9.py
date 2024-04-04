def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	if request.method == 'POST':
		if request.POST['action'] == 'identify':
			return True
		else:
			return False
	else:
		return True