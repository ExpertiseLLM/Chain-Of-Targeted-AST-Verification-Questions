def identify_request(request: RequestType) -> bool:
	if request.headers.get("Authorization") and "Bearer" in request.headers.get("Authorization"):
		return True
	if request.headers.get("User-Agent") and "Matrix" in request.headers.get("User-Agent"):
		return True
	if request.headers.get("X-Matrix-Request-ID"):
		return True
	if request.headers.get("X-Matrix-Client"):
		return True
	return False


