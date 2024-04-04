def identify_request(request: RequestType) -> bool:
	if "HTTP_ORIGIN" not in request.META:
		return False
	if request.META["HTTP_ORIGIN"].startswith("https://matrix.to"):
		return True
	return False

