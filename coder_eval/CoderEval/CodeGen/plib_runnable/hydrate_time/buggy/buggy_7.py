def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if not tz:
		tz = timezone.utc

	return Time(seconds=nanoseconds * tz.utcoffset(None).total_seconds() * 1000.0,
		milliseconds=nanoseconds * tz.utcoffset(None).total_seconds() * 1000.0,
		microseconds=nanoseconds * tz.utcoffset(None).total_seconds() * 1000.0)

