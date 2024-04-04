def identify_request(request: RequestType) -> bool:
	if request.method in ["GET", "POST"] and request.headers.get("User-Agent") == "Matrix/0.0.1":
		if request.path.startswith("/_matrix/"):
			return True
	return False


