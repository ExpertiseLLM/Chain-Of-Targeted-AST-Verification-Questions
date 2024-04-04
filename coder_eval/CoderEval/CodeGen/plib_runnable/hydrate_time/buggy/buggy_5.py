def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if tz is None:
		tz = timezone.utc
	return Time(tz=tz).from_nanoseconds(nanoseconds)

