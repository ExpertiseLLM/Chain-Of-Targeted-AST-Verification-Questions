def identify_request(request: Request) -> bool:
    return isinstance(request, MatrixRequest)
