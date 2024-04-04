def size_to_bytes(size: str) -> int:
    for unit in ["", "K", "M", "G", "T", "P"]:
        if size.endswith(unit):
            return int(float(size[:-len(unit)]))
    raise ValueError("Couldn't convert size to bytes: {}".format(size))
