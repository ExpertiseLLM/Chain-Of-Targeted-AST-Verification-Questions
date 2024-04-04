def _fromutc(self, dt):
	if dt.tzinfo is self._tz:
		return dt
	elif dt.tzinfo is None:
		raise ValueError('dt.tzinfo is None')

	try:
		dst_change = self._tz._utc_transition_times[0]
	except IndexError:
		# No transitions, so we're in standard time.
		return self._fromutc_std(dt)

	if dt < self._tz._utc_transition_times[-1]:
		# The time is unambiguous, so we can return the local time.
		return self._fromutc_std(dt)

	# We have to determine whether the local time is ambiguous or not.
	# This is a little trickier than it seems, because we have to take
	# into account the fact that we might be in a fold.

	# We're going to search for the local time in the transitions,
	# starting from the most recent transition. If we find it, then
	# we've got an ambiguous time, and we'll use the standard algorithm
	
