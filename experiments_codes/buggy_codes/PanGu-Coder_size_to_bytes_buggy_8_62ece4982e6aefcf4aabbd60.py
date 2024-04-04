def size_to_bytes(size: str) -> int:

    """Convert human readable file size to bytes.

Resulting value is an approximation as input value is in most case rounded.

Args:
    size: A string representing a human readable file size (eg: '500K')

Returns:
    A decimal representation of file size

    Examples::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000"""
    size_map = {"M": 1000, "G": 1000000, "T": 1000000000}
    try:
        return int(size) * size_map[size.upper()]
    except KeyError:
        raise ValueError("Not a valid file size")
