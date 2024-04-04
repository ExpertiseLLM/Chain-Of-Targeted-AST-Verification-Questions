def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrator for `Time` and `LocalTime` values.

:param nanoseconds:
:param tz:
:return: Time
	"""
	if time.tzname(tz)!= ('UTC', 'Etc'):
		raise ValueError('tz must be UTC or Etc')
	return Time(nanoseconds=nanoseconds, tz=tz)

