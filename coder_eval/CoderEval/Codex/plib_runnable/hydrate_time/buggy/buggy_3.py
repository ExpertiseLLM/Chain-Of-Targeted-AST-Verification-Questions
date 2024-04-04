def hydrate_time(nanoseconds, tz=None):
	if nanoseconds is None:
		return None
	return Time(nanoseconds // 1000000, nanoseconds % 1000000, tz)


