def hydrate_time(nanoseconds, tz=None):
	if nanoseconds is None:
		return None
	if tz is None:
		return datetime.time(nanoseconds / 1000000000, (nanoseconds % 1000000000) / 1000000)
	else:
		return datetime.time(nanoseconds / 1000000000, (nanoseconds % 1000000000) / 1000000, tzinfo=tz)


