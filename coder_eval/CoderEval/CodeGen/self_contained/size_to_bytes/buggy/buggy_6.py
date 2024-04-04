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
	if size.lower() in ("bytes", "byte", "b"):
		return size
	elif size.lower() in ("KB", "kiloBytes"):
		return int(size.split("K")[0])
	elif size.lower() in ("MB", "megaBytes"):
		return int(size.split("M")[0])
	elif size.lower() in ("GB", "gigaBytes"):
		return int(size.split("G")[0])
	elif size.lower() in ("TB", "teraBytes"):
		return int(size.split("T")[0])
	elif size.lower() in ("PB", "petaBytes"):
		return int(size.split("P")[0])
	elif size.lower() in ("EB", "eByte"):
		return int(size.split("E")[0])
	elif size.lower() in ("ZB", "zettaBytes"):
		return int(size.split("Z")[0])
	elif size.lower() in ("YB", "yottaBytes"):
		return int(size.split("Y")[0])
	else:
		raise Exception("Invalid size: %s" % size)