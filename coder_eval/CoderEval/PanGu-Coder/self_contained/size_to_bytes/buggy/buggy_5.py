def size_to_bytes(size: str) -> int:
    size = size.strip().upper()
    if size == "B":
        return 1
    elif size == "K":
        return 1000
    elif size == "M":
        return 1000000
    elif size == "G":
        return 1000000000
    elif size == "T":
        return 1000000000000
    else:
        raise ValueError("Invalid size: " + size)
