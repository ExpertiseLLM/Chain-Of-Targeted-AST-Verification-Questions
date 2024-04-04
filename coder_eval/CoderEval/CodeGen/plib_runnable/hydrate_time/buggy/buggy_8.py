def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if tz is not None:
		return _time.Time(nanoseconds, tz)
	else:
		return _time.Time(nanoseconds)