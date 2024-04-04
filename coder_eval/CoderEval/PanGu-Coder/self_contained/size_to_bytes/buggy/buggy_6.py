def size_to_bytes(size: str) -> int:
    try:
        return int(size) * 1024
    except ValueError:
        raise ValueError(f"Invalid file size: {size}")