def identify_request(request: dict):
    if 'event' in request:
        return 'event'
    elif'request' in request:
        return'request'
    else:
        return 'unknown'
