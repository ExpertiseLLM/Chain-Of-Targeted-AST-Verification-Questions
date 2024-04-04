def hydrate_time(nanoseconds, tz=None):
	if tz is None:
		return Time(nanoseconds)
	else:
		return LocalTime(nanoseconds, tz)

