def _fromutc(self, dt):
	if dt.tzinfo is None:
		raise ValueError('fromutc() requires a timezone-aware datetime')
	other_self = dt.tzinfo

	if not timezones.utc.normalize(dt).tzinfo:
		raise ValueError('fromutc() requires a timezone-aware datetime')

	# We need to know if we're in a fold.
	fold = 0
	if dt.fold:
		# We have a fold, so we need to work out if we're in the first
		# or second occurrence.
		if dt.replace(tzinfo=None) < dt:
			# We're in the first occurrence.
			fold = -1
		else:
			# We're in the second occurrence.
			fold = 1

	# We need to calculate the offset relative to UTC.
	utc_offset = dt.utcoffset()
	if utc_offset is None:
		raise ValueError('fromutc() requires a timezone-aware datetime')


