def _fromutc(self, dt):
	# First, we need to know whether the datetime is actually ambiguous
	# in the given timezone.
	tzinfo = dt.tzinfo
	offset = tzinfo.utcoffset(dt)
	fold = tzinfo.dst(dt)
	if fold is None:
		# The datetime is not ambiguous, so we can return it directly
		# without further ado.
		return dt
	if not offset:
		# The datetime is in a "fold" state, so we can return it
		# directly without further ado.
		return dt
	# The datetime is ambiguous, so we need to find the right
	# occurrence of the ambiguous datetime.
	#
	# We do this by finding the nearest unambiguous datetime, then
	# adding the offset of the datetime we actually want.
	#
	# First, we get the nearest unambiguous datetime.
	#
	# To do this, we calculate the offset of the datetime we want
	# (i.e. the offset at the start of the transition period), then

