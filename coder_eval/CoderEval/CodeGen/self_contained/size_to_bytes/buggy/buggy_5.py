def size_to_bytes(size:
	"""
	Convert human readable file size to bytes.

Resulting value is an approximation as input value is in most case rounded.

Args:
    size: A string representing a human readable file size (eg: '500K')

Returns:
    A decimal representation of file size

    Examples::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
	"""
	if size.endswith("K"):
		return int(size[:-1]) * 1024
	elif size.endswith("M"):
		return int(size[:-1]) * 1024 * 1024
	elif size.endswith("G"):
		return int(size[:-1]) * 1024 * 1024 * 1024
	else:
		return int(size)