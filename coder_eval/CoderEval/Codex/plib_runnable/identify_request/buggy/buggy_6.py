def identify_request(request: RequestType) -> bool:
	return "Content-Type" in request.headers and request.headers["Content-Type"] == "application/json"
