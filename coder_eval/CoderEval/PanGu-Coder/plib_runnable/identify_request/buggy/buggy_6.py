def identify_request(request: str) -> bool:
    return bool(re.match(REQUEST_IDENTIFIER, request))
