def identify_request(request: RequestType) -> bool:
    """
    Try to identify whether this is a Matrix request
    """
    # noinspection PyBroadException
    try:
        data = json.loads(decode_if_bytes(request.body))
        if "events" in data:
            return True
    except Exception:
        pass
    return False
