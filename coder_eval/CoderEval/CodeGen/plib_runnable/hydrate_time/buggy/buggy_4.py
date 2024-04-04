def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if tz is None:
		return Time()
	tz = tz.utcoffset(None)
	return Time(nanoseconds * nanoseconds, tz)

