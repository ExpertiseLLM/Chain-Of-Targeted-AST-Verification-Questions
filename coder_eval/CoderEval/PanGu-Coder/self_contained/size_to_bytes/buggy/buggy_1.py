def size_to_bytes(size: str) -> int:
    if isinstance(size, float):
        return int(size)

    size = size.lower()
    if size.endswith("g"):
        size = size[:-1]
    if size.endswith("m"):
        size = size[:-1]

    return int(round(float(size) * 1024 ** 3))
