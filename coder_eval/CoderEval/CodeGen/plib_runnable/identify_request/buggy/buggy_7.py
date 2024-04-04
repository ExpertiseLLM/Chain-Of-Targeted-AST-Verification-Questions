def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	try:
		if request.method == 'GET':
			return True
		elif request.method == 'POST':
			if request.POST.get('request_type') =='matrix_request':
				return True
			else:
				return False
	except Exception as e:
		print(e)
		return False