def _fromutc(self, dt):
	if self._tzinfo is None:
		raise ValueError('fromutc: dt.tzinfo is None')

	if dt.tzinfo is None:
		raise ValueError('fromutc: dt.tzinfo is None')

	if not dt.tzinfo.utcoffset(dt) == dt.tzinfo.dst(dt):
		raise ValueError('fromutc: dt.tzinfo is not UTC')

	dtoff = dt.utcoffset()
	if dtoff is None:
		raise ValueError('fromutc: dt.tzinfo is not UTC')

	# calculate the offset from UTC to the new timezone
	# by subtracting the utcoffset from the datetime
	# (which will be zero for UTC)
	dt = dt - dtoff

	# now check to see if the datetime is ambiguous and
	# in a "fold".  if it is, we can't do the conversion
	# because there's no way to know which occurrence
	# of the ambiguous datetime we have
	if
