def identify_request(request: RequestType) -> bool:
	# FIXME: this is a really hacky way of doing it
	# Matrix is supposed to send its user-agent, but the server doesn't seem to send it
	return request.headers.get('X-Matrix-Client-Is') is not None
