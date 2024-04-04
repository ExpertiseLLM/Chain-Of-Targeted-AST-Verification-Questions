def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if tz is None:
		tz = get_current_timezone()
	return Time(nanoseconds * tz.utcoffset(datetime.utcnow()).seconds, tz.tzname(datetime.utcnow()))

