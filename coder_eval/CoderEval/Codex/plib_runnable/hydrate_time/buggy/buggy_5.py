def hydrate_time(nanoseconds, tz=None):
	if nanoseconds is None:
		return None

	if not isinstance(nanoseconds, int):
		raise TypeError("Expected nanoseconds to be an int")

	return Time(nanoseconds // 1000000000, nanoseconds % 1000000000, tz)


