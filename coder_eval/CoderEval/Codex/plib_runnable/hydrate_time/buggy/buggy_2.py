def hydrate_time(nanoseconds, tz=None):
	if not isinstance(nanoseconds, int):
		raise TypeError('nanoseconds must be an integer')
	if tz is None:
		return nanoseconds
	else:
		return datetime.time(nanoseconds // 1000000000, tzinfo=tz)


