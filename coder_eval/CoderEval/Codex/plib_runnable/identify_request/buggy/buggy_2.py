def identify_request(request: RequestType) -> bool:
	return "matrix-org" in request.headers.get("User-Agent", "")


