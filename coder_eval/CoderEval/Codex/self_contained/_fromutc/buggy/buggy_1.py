def _fromutc(self, dt):
		if dt.tzinfo is self:
			return dt

		assert dt.tzinfo is not None

		# Convert dt to UTC.
		dt = dt.astimezone(UTC)

		# Find the offset of the current datetime.
		offset, is_dst, _ = self._utcoffset(dt)

		if not is_dst:
			# No DST, so we can just return the datetime as-is.
			return dt + offset

		# We're in DST, so we need to find the first occurrence
		# of the datetime in local time.
		dt = dt + offset
		start_of_year = self._find_start_of_year(dt.year)
		for dt_offset in (0, 1, -1):
			candidate = dt + timedelta(days=dt_offset)
			is_dst_candidate, _ = self._isdst(candidate, start_of_year)

		
