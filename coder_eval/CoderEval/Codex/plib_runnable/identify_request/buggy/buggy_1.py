def identify_request(request: RequestType) -> bool:
	if request.headers.get("Authorization") and "Bearer" in request.headers["Authorization"]:
		return True
	elif request.query.get("access_token"):
		return True
	return False


