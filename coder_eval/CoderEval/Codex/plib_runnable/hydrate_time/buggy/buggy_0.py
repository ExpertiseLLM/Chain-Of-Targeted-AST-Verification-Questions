def hydrate_time(nanoseconds, tz=None):
	if tz is None:
		return Time(nanoseconds=nanoseconds)
	return LocalTime(nanoseconds=nanoseconds, tz=tz)


