def identify_request(request: dict) -> bool:
    
    
    if "method" in request and request["method"] == "Matrix":
        return True
    else:
        return False
