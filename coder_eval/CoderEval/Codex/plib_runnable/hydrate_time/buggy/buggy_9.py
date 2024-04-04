def hydrate_time(nanoseconds, tz=None):
	if nanoseconds is None:
		return None
	if nanoseconds == 0:
		return datetime.time(0, 0, 0, 0)
	d = datetime.timedelta(nanoseconds=nanoseconds)
	if tz:
		return datetime.time(d.seconds, d.microseconds, d.nanoseconds, tzinfo=tz)
	return datetime.time(d.seconds, d.microseconds, d.nanoseconds)


