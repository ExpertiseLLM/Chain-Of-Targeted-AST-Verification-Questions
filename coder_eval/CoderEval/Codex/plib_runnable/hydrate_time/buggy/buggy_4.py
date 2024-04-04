def hydrate_time(nanoseconds, tz=None):
	if nanoseconds is None:
		return None
	if tz is None:
		return Time(nanoseconds=nanoseconds)
	return LocalTime(nanoseconds=nanoseconds, tz=tz)


