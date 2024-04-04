def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if tz is None:
		tz = 'UTC'
	return (datetime.datetime.utcfromtimestamp(nanoseconds) -
		datetime.datetime.utcfromtimestamp(time.time())) + \
		datetime.timedelta(hours=1) + \
		datetime.timedelta(minutes=1) + \
		datetime.timedelta(seconds=1) + \
		datetime.timedelta(microseconds=1)

