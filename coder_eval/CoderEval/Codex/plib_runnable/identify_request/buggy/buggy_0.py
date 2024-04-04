def identify_request(request: RequestType) -> bool:
	if request.headers.get('User-Agent', '').startswith('Matrix'):
		return True

	if request.headers.get('Authorization', '').startswith('Bearer '):
		return True

	if 'Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json':
		return True

	if 'content-type' in request.headers and request.headers['content-type'] == 'application/json':
		return True

	if 'Content-type' in request.headers and request.headers['Content-type'] == 'application/json':
		return True

	if 'content-Type' in request.headers and request.headers['content-Type'] == 'application/json':
		return True

	return False


