def _fromutc(self, dt):
	if self._tzinfo._cache is None:
		# If the timezone isn't cached, it's impossible to know
		# whether the datetime is ambiguous or not.
		return self.normalize(dt)
	
	dst_offset = self._tzinfo._dst_offset_cache
	utc_offset = self._tzinfo._utc_offset_cache
	
	# Calculate the offset of the datetime, in minutes
	dt_offset = (dt.hour * 60 + dt.minute) * 60 + dt.second
	dt_offset = dt_offset - (utc_offset + dst_offset)
	
	# If the datetime is in a fold, return the first occurrence of the
	# datetime
	if dt.fold and dt_offset < dst_offset:
		dst_offset = 0
	
	return dt.replace(tzinfo=self._tzinfo._tzinfo, fold=dt.fold) + datetime.timedelta(0, dst_offset)


