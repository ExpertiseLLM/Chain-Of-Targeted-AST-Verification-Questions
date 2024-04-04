def identify_request(request: RequestType) -> bool:
	return request.headers.get("User-Agent", "").startswith("Matrix")


