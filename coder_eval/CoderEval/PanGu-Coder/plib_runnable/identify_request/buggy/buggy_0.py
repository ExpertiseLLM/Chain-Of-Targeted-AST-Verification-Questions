def identify_request(request: bytes) -> bool:
    return (
        request[:4] == b'\x00\x01\x00\x00\x00'
        and request[4:] == b'\x00\x01\x00\x00\x00'
        and request[8:12] == b'\x00\x01\x00\x00\x00'
        and request[12:14] == b'\x00\x00\x01\x00\x00'
        and request[14:] == b'\x00\x00\x01\x00\x00'
    )
