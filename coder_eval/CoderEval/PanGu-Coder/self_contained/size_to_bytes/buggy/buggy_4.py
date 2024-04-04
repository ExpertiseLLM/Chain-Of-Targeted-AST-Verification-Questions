def size_to_bytes(size: str) -> int:
    if size is None or size.strip() == '':
        return 0

    return int(round(float(size) / 1024.0, 0))
