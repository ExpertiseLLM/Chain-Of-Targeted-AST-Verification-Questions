def identify_request(request: RequestType) -> bool:
	try:
		if request.headers.get("User-Agent", "").startswith("Python-Matrix-Client"):
			return True
		elif request.headers.get("Origin", "").startswith("https://matrix.org"):
			return True
		elif request.headers.get("Origin", "").startswith("https://matrix.to"):
			return True
		elif request.headers.get("Origin", "").startswith("https://riot.im"):
			return True
		else:
			return False
	except:
		return False


