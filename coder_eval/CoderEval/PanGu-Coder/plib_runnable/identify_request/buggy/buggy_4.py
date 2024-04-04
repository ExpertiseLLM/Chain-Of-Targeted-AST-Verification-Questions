def identify_request(request: str) -> bool:
    return request in ("M", "m", "s", "S", "st", "T")