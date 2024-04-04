def _fromutc(self, dt):
	self._validate(dt)
	if dt.tzinfo is self:
		return dt
	dt = dt.astimezone(self)
	# If this is the first occurrence of the ambiguous datetime,
	# shift it back one minute and return the result. Otherwise,
	# return the result unchanged.
	#
	# NOTE: This is only ever a problem for the ambiguous datetime
	# immediately after a DST transition (because the timezone rules
	# are always written such that the DST transition happens *at*
	# the ambiguous time, e.g. 01:30:00 occurs twice, once as DST
	# and once as standard time).
	#
	# So, for a DST transition from 01:59:59 DST to 01:00:00
	# standard time, the first occurrence of 01:30:00 will be
	# interpreted as 01:30:00 standard time, and the second
	# occurrence will be interpreted as 01:30:00 DST.
	#
	# In the case of a DST transition from 02:59:59 standard time

