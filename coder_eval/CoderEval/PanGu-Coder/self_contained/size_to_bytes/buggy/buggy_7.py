def size_to_bytes(size: str) -> int:
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z", "Y"):
        if size.endswith(unit):
            size = size[:-len(unit)]
            return int(float(size) * 1024 ** 3)
    raise ValueError("Invalid size string: %s" % size)
